from django.urls import path
from .views import all_books, new_book, edit_book, delete_book, my_custom_list, book_detail, book_fetch_detail, add_to_favorite

urlpatterns = [
    path("all/", all_books, name="all_books"),
    path("new/", new_book, name="new_book"),
    path("edit/<slug:slug>/", edit_book, name="edit_book"),
    path("delete/<slug:slug>", delete_book, name="delete_book"),
    path("detail/<slug:slug>", book_detail, name="book_detail"), # change str to int
    path("my-list", my_custom_list, name="my_custom_list"),
    path("fetched-book-detail/<str:id>", book_fetch_detail, name="book_fetch_detail"),
    #
    path("add-to-favorite/", add_to_favorite, name="add_to_favorite")
]
