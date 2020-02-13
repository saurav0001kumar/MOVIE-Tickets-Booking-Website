from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class movies(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="pics",default="default.png")
    date=models.DateField()
    duration=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    language=models.CharField(max_length=50)
    rating=models.CharField(max_length=50)
    cast=models.TextField(max_length=100)
    trailer=models.CharField(max_length=100)
    up=models.BooleanField(default=False)
    price=models.IntegerField(default=0)

class movies2(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="pics",default="default.png")
    date=models.DateField()
    duration=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    language=models.CharField(max_length=50)
    rating=models.CharField(max_length=50)
    cast=models.TextField(max_length=100)
    trailer=models.CharField(max_length=100)
    up=models.BooleanField(default=False)
    price=models.IntegerField(default=0)

class reg(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=100)
    mobile=models.IntegerField()
    age=models.IntegerField()
    seats=models.IntegerField()
    