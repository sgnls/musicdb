import re

from django.db.models import fields

from musicdb.utils import slugify

class DenormalisedCharField(fields.CharField):
    def __init__(self, attr, *args, **kwargs):
        # Set a longer max_length by default
        kwargs['max_length'] = kwargs.get('max_length', 100)
        kwargs['db_index'] = kwargs.get('db_index', True)
        kwargs['editable'] = kwargs.get('editable', False)

        super(DenormalisedCharField, self).__init__(*args, **kwargs)

        self.attr = attr

    def pre_save(self, obj, add):
        val = getattr(obj, self.attr)

        if callable(val):
            val = val()

        return val[:self.max_length]

    def south_field_triple(self):
        from south.modelsinspector import introspector
        args, kwargs = introspector(self)
        return ('django.db.models.fields.TextField', args, kwargs)

class MySlugField(DenormalisedCharField):
    def __init__(self, *args, **kwargs):
        self.filter = kwargs.pop('filter', None)

        super(MySlugField, self).__init__(*args, **kwargs)

    def pre_save(self, obj, add):
        val = super(MySlugField, self).pre_save(obj, add)
        val = slugify(val)[:self.max_length]

        val_to_prepend = val[:self.max_length - 3]

        qs = obj.__class__.objects.all()

        if self.filter is not None:
            qs = getattr(obj, self.filter)()

        count = 1
        while count <= 999:
            filters = {
                self.name: val,
            }

            if not qs.filter(**filters).exclude(pk=obj.pk).exists():
                return val

            val = '%s-%d' % (val_to_prepend, count)
            count += 1

        assert False

class FirstLetterField(DenormalisedCharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 1

        super(FirstLetterField, self).__init__(*args, **kwargs)

    def pre_save(self, obj, add):
        val = super(FirstLetterField, self).pre_save(obj, add).lower()

        if re.match(r'[a-z]', val):
            return val

        if re.match(r'\d', val):
            return '0'

        return '-'
