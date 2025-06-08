from django.views.generic import ListView, DetailView
from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'list_book.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'detail_book.html'
