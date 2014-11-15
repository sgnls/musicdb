from django import forms

from ..models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = (
            'last_name',
            'first_names',
        )

class MergeForm(forms.Form):
    duplicate = forms.ModelChoiceField(
        queryset=Author.objects.none()
    )

    def __init__(self, original, *args, **kwargs):
        self.original = original

        super(MergeForm, self).__init__(*args, **kwargs)

        self.fields['duplicate'].queryset = Author.objects.exclude(
            pk=original.pk,
        )

    def save(self):
        duplicate = self.cleaned_data['duplicate']

        for x in duplicate.books.all():
            x.author = self.original
            x.save()

        duplicate.delete()

        return self.original
