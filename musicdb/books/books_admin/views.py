from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from musicdb.utils.decorators import superuser_required

from ..models import Author

from .forms import AuthorForm

@superuser_required
def author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)

    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)

        if form.is_valid():
            form.save()

            messages.success(request, "Author saved.")

            return redirect('books:admin:author', author.pk)
    else:
        form = AuthorForm(instance=author)

    return render(request, 'books/admin/author.html', {
        'form': form,
        'author': author,
    })
