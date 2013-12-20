from django.contrib import admin

from .models import Author, Book

class AuthorAdmin(admin.ModelAdmin):
    search_fields = (
        'first_names',
        'last_name',
    )
    fields = (
        'last_name',
        'first_names',
    )
admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    fields = (
        'title',
    )
    search_fields = ('title',)
admin.site.register(Book, BookAdmin)
