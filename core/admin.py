from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ["title", "description", "publish_date", "rating", "book_cover"]
    list_display = ["title", "publish_date", "rating"]
    list_filter = ["publish_date", "rating"]
    search_fields = ["title", "description"]

