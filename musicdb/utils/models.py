from django.template import add_to_builtins

for x in (
    'fonts',
    'media',
):
    add_to_builtins('musicdb.utils.templatetags.%s' % x)
