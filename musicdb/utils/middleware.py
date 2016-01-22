import sys

from django.conf import settings
from django.views.debug import technical_500_response
from django.core.exceptions import MiddlewareNotUsed

class ShowForSuperusersMiddleware(object):
    """
    Shows the "technical" 500 error page instead of the "friendly" error if the
    user making the request is a superuser.

    This gives the appearance of not having ``settings.DEBUG`` disabled on the
    live site.

    This was inspired by `http://www.djangosnippets.org/snippets/935/`_.
    """

    def __init__(self):
        if settings.DEBUG:
            raise MiddlewareNotUsed()

    def process_exception(self, request, exception):
        if not request.user.is_superuser:
            return

        return technical_500_response(request, *sys.exc_info())
