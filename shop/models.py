from django.db import models
from django.db.models.base import Model

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discounted = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()

    # we're going to use the url and load the image, like many other sites do
    image = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.title

class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.CharField(max_length=200)