from django.shortcuts import render
from .models import Book, Category

# Create your views here.


def main(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    context = {"books": books, "categories": categories}
    return render(request, "dashboard/main.html", context)


def books(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "dashboard/books.html", context)


def delete_book(request, slug):
    return render(request, "dashboard/delete_book.html")


def update(request, slug):
    return render(request, "dashboard/update.html")
