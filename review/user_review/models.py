from django.db import models

# Create your models here.
class UserReview(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField()
    #owner_comment = models.TextField()

    class Meta:
        db_table = 'User Review'