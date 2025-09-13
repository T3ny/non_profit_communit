from django.db import models
from django.contrib.auth.models import AbstractUser

class users(AbstractUser):
    # storing TextField
    bio =  models.TextField(blank=True, null=True)
    # storing profile
    profile =  models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None, blank = True , null= True)
    # storing short text for company and location
    organisations = models.CharField(max_length=235 ,  blank=True, null=True)
    location  =  models.CharField(max_length=235 ,  blank=True , null=True)

#This makes the admin panel show the user’s username instead of “User object(1)”
    def __str__(self):
        return self.username