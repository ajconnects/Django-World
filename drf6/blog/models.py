from django.db import models

# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.tag


class Post(models.Model):
    title = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)
