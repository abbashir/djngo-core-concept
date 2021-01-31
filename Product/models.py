from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=220)
    stock = models.IntegerField()
    price = models.FloatField(max_length=100)
    description = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title  # you can use smart_text method
