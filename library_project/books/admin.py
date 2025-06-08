from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'year', 'genre')
    search_fields = ('title', 'author', 'genre')
    list_filter = ('year', 'genre')
    list_display_links = ('id', 'title')
