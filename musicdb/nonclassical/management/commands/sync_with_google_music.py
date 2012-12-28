import collections

from gmusicapi.api import Api

from django.core.management.base import NoArgsCommand
from django.conf import settings

from musicdb.utils.progress import progress_qs

from musicdb.nonclassical.models import Album

class Command(NoArgsCommand):
    """
    TODO: Store Google's ID locally so we merely need to update metadata.
    """

    def handle_noargs(self, **options):
        print "I: Logging in..."
        api = Api()
        assert settings.GOOGLE_MUSIC_PASSWORD, "No password setup"

        api.login(
            settings.GOOGLE_MUSIC_EMAIL,
            settings.GOOGLE_MUSIC_PASSWORD,
        )

        if not api.is_authenticated():
            print "E: Could not authenticate"
            return

        all_tracks = dict((x['id'], x) for x in api.get_all_songs())

        tracks = collections.defaultdict(
            lambda: collections.defaultdict(dict)
        )

        for track in all_tracks.values():
            tracks[track['artist']][track['album']][track['name']] = track

        to_upload = set()
        already_uploaded = set()

        print "I: Calculating differences"
        for album in progress_qs(Album.objects.all()):
            for cd in album.cds.all():
                for track in cd.tracks.all():
                    try:
                        metadata = tracks[album.artist.name][album.title][track.title]
                        already_uploaded.add(metadata['id'])
                    except KeyError:
                        to_upload.add(track)

        to_delete = [x for x in all_tracks.keys() if x not in already_uploaded]

        print "%d tracks to delete" % len(to_delete)
        print "%d track(s) to upload" % len(to_upload)
        print "%d tracks already uploaded" % len(already_uploaded)

        print "I: Deleting %d track(s)..." % len(to_delete)
        api.delete_songs(to_delete)

        print "I: Uploading %d track(s)..." % len(to_upload)
        for track in to_upload:
            filename = track.music_file.file.absolute_location()

            response = api.upload([filename])

            assert response, "Upload failed"

            track_id = response.values()[0]

            api.change_song_metadata([{
                'id': response.values()[0],
                'year': track.cd.album.year or '',
                'name': track.title,
                'album': track.cd.album.title,
                'artist': track.cd.album.artist.name,
                'albumArtist': track.cd.album.artist.name,
                'track': track.num,
                'disc': track.cd.num,
                'totalDiscs': track.cd.album.cds.count(),
                'totalTracks': track.cd.tracks.count(),
            }])

        print "I: Logging out.."

        api.logout()
