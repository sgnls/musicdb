from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()

TEMPLATE = '<link href="//fonts.googleapis.com/css?family=%s" rel="stylesheet">'

@register.simple_tag
def font(definition):
    if not settings.FONTS_ENABLED:
        return ''

    return mark_safe(TEMPLATE % definition)
