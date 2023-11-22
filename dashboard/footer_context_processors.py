from .models import *
from .forms import CategoryForm


def sidebar(request):
    books = Book.objects.all()
    category_form = CategoryForm()
    context = {
        "categories": Category.objects.all(),
        "category_form": category_form,
        "books": books,
    }
    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
    return context
