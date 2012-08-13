from django_enumfield import make_enum, Item

PlaylistFormatEnum = make_enum('PlaylistFormatEnum',
    Item(0, 'xspf', "XSPF"),
    Item(1, 'm3u', "M3U"),
)
