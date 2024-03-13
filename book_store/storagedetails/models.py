from typing import Iterable
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Country(models.Model):  #many to many relation
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = "Countries Name"
        db_table = "Author Published"

    def __str__(self) -> str:
        return f"{self.name}, Code: {self.code}."


class Address(models.Model):   #one to one relation
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Address Entries"
        db_table = "Author Address"

    def __str__(self) -> str:
        return f"{self.postal_code}, {self.street}, {self.city}."


class Author(models.Model):   #one to many relation
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return self.full_name()
    
    class Meta:
        db_table = "Author Details"


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books') #related_name is to change relation name(book_set)
    #author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    published_countries = models.ManyToManyField(Country)

    class Meta:
        db_table = "Author Books info"

    def get_absolute_url(self):
        return reverse("book-details", args=[self.slug])
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"
    
