from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=200)
    product_price = models.IntegerField()
    product_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.product_name


class Items(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.stock} x {self.product.product_name}'
