from django import forms
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
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
