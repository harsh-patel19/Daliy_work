

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from myapp.manager import CustomUserManager
# Create your models here.

class CustomeUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=15,unique=True)
    bio = models.TextField(blank=True, null=True)

    USERNAME_FIELD ='phone_number'
    REQUIRED_FIELDS =[]

objects = CustomUserManager()