from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RecipeModel(models.Model):
    imageURL = models.CharField(max_length=800, default="")
    meal = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, default="")
    Creator = models.CharField(max_length=200)
    ingredients = models.TextField(max_length=2000,default="")
    directions = models.TextField(max_length=2000, default="")

# USER MODEL
class CreatorModel(models.Model):
    username = models.CharField(max_length=20)
    password1 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)
    userForeignKey = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, unique=True)

    # TO DISPLAY USERNAME IN ADMIN SITE
    def __str__(self):
        return self.username
