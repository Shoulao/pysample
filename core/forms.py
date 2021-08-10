from django.forms import ModelForm
from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "description", "publish_date", "rating", "book_cover"]
