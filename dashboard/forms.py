from django import forms
from .models import Book, Category


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        exclude = ["slug"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
