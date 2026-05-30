from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.IntegerField()
    dec = models.TextField()
    image = models.ImageField(upload_to="image/",blank=True,null=True)


