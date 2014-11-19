from email_from_template import send_mail

from django import forms
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
        )

    def save(self):
        password = get_random_string(8)

        instance = super(NewUserForm, self).save(commit=False)
        instance.set_password(password)
        instance.save()

        send_mail((instance.email,), 'auth/admin/new_user.email', {
            'user': instance,
            'password': password,
        })

        return instance

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
        )

class ResetPasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
        )

    def save(self):
        password = get_random_string(8)

        self.instance.set_password(password)
        self.instance.save()

        return password
