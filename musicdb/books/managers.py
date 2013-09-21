from django.db import models

class AuthorManager(models.Manager):
    def letters(self):
        return self.values_list('last_name_first', flat=True) \
            .order_by('last_name_first').distinct()
