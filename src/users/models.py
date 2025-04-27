from django.db import models
from django.contrib.auth.models import User
from localflavor.mx.models import MXStateField

from .utils import user_directory_path

# Create your models here.

class Location(models.Model):
    address_1 = models.CharField(max_length=120)
    address_2 = models.CharField(max_length=120, blank=True)
    city = models.CharField(max_length=64)
    state = MXStateField(default='DF')
    zip_code = models.CharField(max_length=5,blank=True)

    def __str__(self):
        return f'Location {self.id}'

class Profile(models.Model):
    # one to one field create a one to one relationship with the user model
    # this means that each user can have only one profile and each profile can belong to only one user 
    user = models.OneToOneField(User, on_delete=models.CASCADE)#in cascade means that if the user is 
    # deleted, the profile will also be deleted
    photo = models.ImageField(null=True, blank=True, upload_to=user_directory_path)
    bio = models.CharField(max_length=140, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    location = models.OneToOneField(Location,on_delete=models.SET_NULL,null=True)

    #this method is used to return a string representation of the model
    def __str__(self):
        return f'{self.user.username}\'s Profile'
