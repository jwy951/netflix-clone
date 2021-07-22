from django.db import models
from django.contrib.auth.models import AbstractUser,User
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

from django.db.models.signals import pre_delete

import datetime as dt

# Create your models here.
AGE_CHOICES=(('All','All'), ('Kids','Kids'))

MOVIE_TYPE=(
    ('single','Single'),
    ('seasonal','Seasonal'))

class CustomUser(User):
    profiles = models.ManyToManyField('Profile')
    
class Profile(models.Model):
    name = models.CharField(max_length=255)
    age_limit = models.CharField(max_length=255)
    uuid = models.UUIDField(default=uuid.uuid4,unique=True)
    
    def __str__(self):
        return self.name + "" + self.age_limit
    
    
class Movie(models.Model):
    title:str=models.CharField(max_length=225)
    description:str=models.TextField()
    created =models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4,unique=True)
    type=models.CharField(max_length=10,choices=MOVIE_TYPE)
    videos=models.ManyToManyField('Video')
    flyer=models.ImageField(upload_to='flyers',blank=True,null=True)
    age_limit=models.CharField(max_length=5,choices=AGE_CHOICES,blank=True,null=True)

class Video(models.Model):
    title:str = models.CharField(max_length=225,blank=True,null=True)
    file=models.FileField(upload_to='movies')
    