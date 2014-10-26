from django.template import add_to_builtins

for x in (
    'bootstrap',
    'fonts',
    'media',
    'pagination',
):
    add_to_builtins('musicdb.utils.templatetags.%s' % x)
