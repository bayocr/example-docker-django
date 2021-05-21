from django.contrib import admin

from .models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'count_books']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'page_number', 'author', 'published_at']
    list_filter = ['author', 'page_number']