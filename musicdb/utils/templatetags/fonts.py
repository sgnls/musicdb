from django import template
from django.conf import settings

register = template.Library()

TEMPLATE = '<link href="//fonts.googleapis.com/css?family=%s" rel="stylesheet">'

@register.simple_tag
def font(definition):
    if not settings.FONTS_ENABLED:
        return ''

    return TEMPLATE % definition
