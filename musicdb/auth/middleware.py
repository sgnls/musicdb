from django.shortcuts import redirect
from django.core.urlresolvers import reverse

class RequireLoginMiddleware(object):
    ALLOW = (
        '/media/',
        '/admin',
        '/__debug__/',
    )

    def process_view(self, request, fn, *args, **kwargs):
        for prefix in self.ALLOW:
            if request.path.startswith(prefix):
                return

        if request.user.is_authenticated():
            return

        if getattr(fn, 'login_not_required', False):
            return

        return redirect('%s?next=%s' % (reverse('auth:login'), request.path))
