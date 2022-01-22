from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Avg

from .models import Book

# Create your views here.
def index(request):
    all_books = Book.objects.all().order_by("-title")
    total_books = all_books.count()
    avg_rating = all_books.aggregate(Avg("rating"))

    return render(request, "book_outlet/index.html", {
        "books": all_books,
        "total_books_count": total_books,
        "avg_rating": avg_rating
    })

def book_detail(request, id):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()

    book = get_object_or_404(Book, pk=id)
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
    })

def book_detail_by_slug(request, slug):
    # try:
    #     book = Book.objects.get(slug=slug)
    # except:
    #     raise Http404()

    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
    })