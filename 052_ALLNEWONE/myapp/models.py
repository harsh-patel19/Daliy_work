from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.IntegerField()
    manudate = models.DateField()
    enddate = models.DateField()
    image = models.ImageField(upload_to='images/',blank=True,null=True)

    