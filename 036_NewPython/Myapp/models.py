from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to="images/",blank=True,null=True)