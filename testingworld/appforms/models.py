from django.db import models

# Create your models here.
class UserApplication(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateTimeField()
    rating = models.IntegerField(null=True)

    class Meta:
        db_table = 'User Application'