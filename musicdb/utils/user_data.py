from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User

INSTANCES = []

def PerUserData(related_name=None):
    """
    Class factory that returns an abstract model attached to a ``User`` object
    that creates and destroys concrete child instances where required.

    Example usage::

        class ToppingPreferences(PerUserData('toppings')):
            pepperoni = models.BooleanField(default=True)
            anchovies = models.BooleanField(default=False)

        >>> u = User.objects.create_user('test', 'example@example.com')
        >>> u.toppings  # ToppingPreferences created automatically
        <ToppingPreferences: user=test>
        >>> u.toppings.anchovies
        False
    """

    class UserDataBase(models.base.ModelBase):
        def __new__(mcs, name, bases, attrs):
            model = super(UserDataBase, mcs).__new__(mcs, name, bases, attrs)

            if model._meta.abstract:
                return model

            def on_create(sender, instance, created, *args, **kwargs):
                if created:
                    model.objects.create(user=instance)

            def on_delete(sender, instance, *args, **kwargs):
                model.objects.filter(pk=instance).delete()

            post_save.connect(on_create, sender=User, weak=False)
            pre_delete.connect(on_delete, sender=User, weak=False)

            INSTANCES.append(model)

            return model

    class UserData(models.Model):
        user = models.OneToOneField(
            'auth.User',
            primary_key=True,
            related_name=related_name,
        )

        __metaclass__ = UserDataBase

        class Meta:
            abstract = True

        def __unicode__(self):
            return 'user=%s' % self.user.username

    return UserData

def lint():
    for model in INSTANCES:
        qs = User.objects.filter(**{
            '%s__pk__isnull' % model.user.field.related_query_name(): True,
        })

        if not qs.exists():
            continue

        print "W: %d users are missing %s instances: %r" % (
            qs.count(),
            model,
            qs,
        )
