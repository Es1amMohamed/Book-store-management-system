from django.shortcuts import redirect, render
from .models import Book, Category
from .forms import BookForm, CategoryForm

# Create your views here.


def main(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    form = BookForm()
    all_books = Book.objects.filter(active=True).count()
    sold_books = Book.objects.filter(status="sold").count()
    rented_books = Book.objects.filter(status="rented").count()
    available_books = Book.objects.filter(status="available").count()

    context = {
        "books": books,
        "categories": categories,
        "form": form,
        "all_books": all_books,
        "sold_books": sold_books,
        "rented_books": rented_books,
        "available_books": available_books,
    }
    if request.method == "POST":
        form_book = BookForm(request.POST, request.FILES)
        if form_book.is_valid():
            form_book.save()
            return render(request, "dashboard/main.html", context)

    return render(request, "dashboard/main.html", context)


def books(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "dashboard/books.html", context)


def delete_book(request, slug):
    book = Book.objects.get(slug=slug)
    if request.method == "POST":
        book.delete()
        return redirect("/")

    return render(request, "dashboard/delete.html")


def update(request, slug):
    book = Book.objects.get(slug=slug)
    form = BookForm(instance=book)
    context = {"book": book, "form": form}
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, "dashboard/update.html", context)
