from django import template
from django.utils.safestring import mark_safe

register = template.Library()

"""
Easily create responsive Bootstrap 3 grids in Django.

Usage
=====

    <div class="container">
      {% for obj in mylist %}

      {% grid_clearfix xs=1 lg=6 %}

      <div class="{% grid_classes xs=1 lg=6 %}">
        {{ obj.name }}
      </div>
    </div>

Arguments can be either be positional, eg:

    {% grid_classes 1 3 4 4 %}
    {% grid_clearfix 1 3 4 4 %}

or kwargs:

    {% grid_classes xs=1 sm=3 md=3 lg=4 %}
    {% grid_clearfix xs=1 sm=3 md=3 lg=4 %}

Arguments are optional - larger breakpoints will inherit from their parent. For
example:

    {% grid_classes xs=1 sm=3 lg=6 %}
    {% grid_clearfix xs=1 sm=3 lg=6 %}

.. is equivalent to the more explicit

    {% grid_classes xs=1 sm=3 md=3 lg=3 %}
    {% grid_clearfix xs=1 sm=3 md=3 lg=3 %}
"""

@register.simple_tag(takes_context=True)
def grid_classes(context, *args, **kwargs):

    classes = []

    for _, breakpoint, cols in _get_cols(context, *args, **kwargs):
        classes.append('col-%s-%d' % (breakpoint, 12 / cols))

    return ' '.join(classes)

@register.simple_tag(takes_context=True)
def grid_clearfix(context, *args, **kwargs):
    classes = []

    for idx, breakpoint, cols in _get_cols(context, *args, **kwargs):
        if idx and idx % cols == 0:
            classes.append('visible-%s' % breakpoint)

    if not classes:
        return ''

    return mark_safe('<div class="clearfix %s"></div>' % ' '.join(classes))

def _get_cols(context, xs=12, sm=None, md=None, lg=None):
    try:
        idx = context['forloop']['counter0']
    except KeyError:
        raise template.TemplateSyntaxError("Not called from within forloop.")

    for breakpoint, cols in (('xs', xs), ('sm', sm), ('md', md), ('lg', lg)):
        # Avoid superfluous classes; let Bootstrap deal with inheritance
        if not cols:
            continue

        yield idx, breakpoint, int(cols)
