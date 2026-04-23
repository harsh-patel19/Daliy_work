from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    image = models.ImageField(upload_to='images/',null=True,blank=True)