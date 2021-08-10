import random
import string

from django.db import models
from django.utils.text import slugify


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class Book(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    publish_date = models.DateField(null=True, blank=True)
    description = models.TextField(default="description", max_length=250)
    rating = models.DecimalField(max_digits=1, decimal_places=0, null=True, blank=True)
    book_cover = models.ImageField(upload_to="book_covers", null=True, blank=True)
    slug = models.SlugField(max_length=64, unique=True)

    def __str__(self):
        return self.title_with_pub_date()

    def slug_value(self):
        return self.title

    def title_with_pub_date(self):
        return f"{self.title} ({self.publish_date.year})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{rand_slug()} - {self.title}')
        super(Book, self).save(*args, **kwargs)
