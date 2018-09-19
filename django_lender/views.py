from django.shortcuts import render, get_object_or_404
from .models import Book
# Create your views here.


def book_list_view(request):
    books = Book.objects.all()

    context = {
        'book': books
    }

    return render(request, 'book/book_list.html', context=context)


def book_detail_view(request, pk=None):
    books = get_object_or_404(Book, id=pk)
    context = {
        'book': books,
    }

    return render(request, 'book/book_detail.html', context)
