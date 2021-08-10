from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm
from .api import get_initial_data, get_single_volume
from django.http import JsonResponse

import json


def all_books(request):
    data = get_initial_data()
    books = data["items"]
    return render(request, "books.html", {"books": books})


@login_required
def my_custom_list(request):
    books = Book.objects.all()
    return render(request, "my_custom_list.html", {"books": books})


@login_required
def new_book(request):
    form = BookForm(request.POST or None, request.FILES or None)
    button_text = "create"
    page_title = "add new book"

    if form.is_valid():
        form.save()
        return redirect(all_books)

    return render(request, "book_form.html", {"form": form,  "button_text": button_text, "page_title": page_title})


@login_required
def edit_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    form = BookForm(request.POST or None, request.FILES or None, instance=book)
    button_text = "save"
    page_title = "edit book"

    if form.is_valid():
        form.save()
        return redirect(all_books)

    return render(request, "book_form.html", {"form": form, "button_text": button_text, "page_title": page_title})


@login_required
def delete_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    button_text = "delete"
    page_title = "delete book"

    if request.method == "POST":
        book.delete()
        return redirect(all_books)

    return render(request, "confirm_delete.html", {"book": book, "button_text": button_text, "page_title": page_title})


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    page_title = book.title

    return render(request, "book_detail.html", {"book": book})


def book_fetch_detail(request, id):
    book = get_single_volume(id)

    return render(request, "book_fetch_detail.html", {"book": book})


def add_to_favorite(request):
    if request.method == "POST":

        content = json.loads(request.body)
        print(dir(request))
        print(request.user)
        print(content)
        return JsonResponse({"data": "ok"}, status=200)
    else:
        return JsonResponse({"error": "Error"}, status=400)
