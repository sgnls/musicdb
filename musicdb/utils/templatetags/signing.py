from django import template

from django.core.signing import Signer, BadSignature

register = template.Library()

@register.filter
def sign(value):
    return Signer().sign(value)
