from django.template import add_to_builtins

for x in (
    'bootstrap',
    'fonts',
    'media',
    'pagination',
    'signing',
):
    add_to_builtins('musicdb.utils.templatetags.%s' % x)

add_to_builtins('django_autologin.templatetags.django_autologin')
