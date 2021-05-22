from django.views.generic import ListView, DetailView

from .models import Author, Book

class BookListView(ListView):
    model = Book
    paginate_by = 6
    

    def get_queryset(self):
        queryset = Book.objects.all()

        return queryset


class BookDetailView(DetailView):
    queryset = Book.objects.all()