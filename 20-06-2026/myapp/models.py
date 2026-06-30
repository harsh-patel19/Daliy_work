from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images/',blank=True,null=True)


    def __str__(self):
        return self.name