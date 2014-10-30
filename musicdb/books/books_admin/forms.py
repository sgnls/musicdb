from django import forms

from ..models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = (
            'last_name',
            'first_names',
        )
