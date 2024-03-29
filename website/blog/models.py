from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email_address = models.EmailField()

    class Meta:
        db_table = "Post info"
        verbose_name_plural = "Author Details"


    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self) -> str:
        return self.fullname()


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt= models.TextField(validators =[MinLengthValidator(10)])
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators =[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
    tag = models.ManyToManyField(Tag)

    class Meta:
        db_table = "Post Details"
        verbose_name_plural = "The Post"

    def __str__(self) -> str:
        return f"{self.title} {self.date}"
