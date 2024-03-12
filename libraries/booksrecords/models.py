from typing import Iterable
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Author(models.Model):
    pass



class BooksDetails(models.Model):
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=70)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=50)
    title = models.CharField(max_length=50, default=True)
    rating = models.IntegerField(default=True,
        validators = [
            MinValueValidator(1), MaxValueValidator(9)
        ])
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)  #very importance (editable=False was remove because on the admin i use the readonly field)

    class Meta():
        db_table = "Receiver info"

    def __str__(self) -> str:
        return f"{self.title.title()}: {self.fullname.title()}, {self.address.title()}, {self.email.title()}, {self.phone} and book={self.rating}."
    
    def get_absolute_url(self):
        return reverse("details", args=[self.slug])
    
    #i am using the prepopulated field to overwrite the save 
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
