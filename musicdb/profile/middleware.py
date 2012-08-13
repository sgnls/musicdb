from .models import Profile

class ProfileMiddleware(object):
    def process_view(self, request, fn, *args, **kwargs):
        if not request.user.is_authenticated():
            return

        try:
            request.profile = Profile(**request.session['profile'])
        except KeyError:
            request.profile = Profile()
