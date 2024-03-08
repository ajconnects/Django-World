from django.db import models

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

    class Meta:
        db_table = 'student'