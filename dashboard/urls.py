from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.main, name="main"),
    path("books/", views.books, name="books"),
    path("delete_book/<slug:slug>/", views.delete_book, name="delete_book"),
    path("update/<slug:slug>/", views.update, name="update"),
]
