from django.db import models

# Create your models here.

class FormModel(models.Model):
    name = models.CharField(unique = True, max_length = 200)
    favorite_color = models.CharField(max_length = 200)
    cats_or_dogs = models.TextField()
