from django_enumfield import EnumField

from django.db import models

from musicdb.utils.user_data import PerUserData

class Profile(PerUserData('profile')):
    kindle_email_address = models.EmailField(blank=True)
