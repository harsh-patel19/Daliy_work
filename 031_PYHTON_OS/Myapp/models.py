from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.IntegerField()
    image = models.ImageField(upload_to='images/',blank=True,null=True)

    