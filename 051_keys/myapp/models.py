from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    decrib = models.TextField()
    price = models.IntegerField()
    qty = models.IntegerField()
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    
    def __str__(self):
        return self.name