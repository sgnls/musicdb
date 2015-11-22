from django import template

from django.core.signing import Signer

register = template.Library()

@register.filter
def sign(value):
    return Signer().sign(value)
