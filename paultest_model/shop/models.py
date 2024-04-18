from django.db import models

class MyManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        qs = super().get_queryset()
        return qs.filter(firstname="")

# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    # age = models.PositiveIntegerField()
    # json = models.JSONField()
    # webpage = models.URLField()
    # photo = models.BinaryField()
    # active = models.BooleanField()
    stock = models.IntegerField()
    # new_field = models.CharField("A label for my field", max_length=40,)
    # images = models.ImageField("Upload your images", upload_to="/images/")
    # email = models.TextField("Please provide your comment", Null=True)


    objects = models.Manager()
    tablets = MyManager()

    class Meta:
        db_table = 'student'

    def __str__(self) -> str:
        return f"{self.firstname}-{self.lastname}-{self.email}."