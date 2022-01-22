from django.db import models

# Create your models here.
class Review(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.IntegerField()