from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    ROLE_CHOICE = (
        ('admin','Admin'),
        ('teacher','Teacher'),
        ('student','Student'),

    )

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()

    role = models.CharField(max_length=20,choices=ROLE_CHOICE)
    image  = models.ImageField(upload_to='images/',null=True,blank=True)

    def __str__(self):
        return self.name