from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Employee(models.Model):
    ROLE_CHOICES = (
        ('admin','Admin'),
        ('employee','Employee'),
    )

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    role = models.CharField(max_length=20,choices=ROLE_CHOICES)
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    
    def __str__(self):
        return self.name