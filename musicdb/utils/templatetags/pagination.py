from django import template

register = template.Library()

@register.filter
def paginator(querydict, page_number):
    querydict = querydict.copy()
    querydict['page'] = page_number

    if page_number == 1:
        querydict.pop('page')

    return querydict.urlencode()
