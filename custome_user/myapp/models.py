from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
from myapp.manager import *

# Create your models here.

class Customeuser(AbstractUser):
    username=None
    phone_number=models.CharField(max_length=50,unique=True)
    email=models.CharField(max_length=50)
    user_bio=models.CharField(max_length=50)
    user_profile=models.ImageField(upload_to="profile")

    # groups=models.ManyToManyField(
    #     Group,
    #     related_name="custome_groups",
    #     blank=True
    # )

    # user_permissions=models.ManyToManyField(
    #     Permission,
    #     related_name="customeuser_permissions",
    #     blank=True
    # )

    USERNAME_FIELD='phone_number'
    REQUIRED_FIELDS=[]
    objects=UserManager()
