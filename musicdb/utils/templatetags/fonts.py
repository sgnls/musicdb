from django import template
from django.conf import settings

register = template.Library()

GOOGLE_FONT_TEMPLATE = '<link href="//fonts.googleapis.com/css?family=%s" rel="stylesheet">'

@register.simple_tag
def google_font(definition):
    if not settings.FONTS_ENABLED:
        return ''

    return GOOGLE_FONT_TEMPLATE % definition
