from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class UserProfile(models.Model):
    user_name = models.CharField(max_length=200)
    user_bio = models.TextField()
    profile_pic = models.ImageField(upload_to='media/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_name

    def edit(self, user_name, user_bio, profile_pic):
        self.user_name = user_name
        self.user_bio = user_bio
        self.profile_pic = profile_pic
        self.save()

class Cottage(models.Model):
    cottage_name = models.CharField(max_length=255, unique=True)
    cottage_description = models.TextField()
    cottage_location = models.CharField(max_length=255)
    cottage_capacity = models.IntegerField()
    cottage_image = models.ImageField(upload_to='images/', null=True, blank=True)
    cottage_price = models.IntegerField()





class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cottage = models.ForeignKey(Cottage, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    stock = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.stock} x {self.cottage.cottage_name}'

class Payment(models.Model):
    phone_number = models.CharField(max_length=11, unique=True),
    amount = models.IntegerField()
