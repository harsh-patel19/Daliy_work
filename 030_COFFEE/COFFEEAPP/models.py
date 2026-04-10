from django.db import models
from django.contrib.auth.models import AbstractUser
from COFFEEAPP.manager import CustomeManager

class Customeuser(AbstractUser):
    username=None
    phone=models.CharField(max_length=20,unique=True)
    full_name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    password=models.CharField()


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['phone']
    objects=CustomeManager()



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    Category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=8,decimal_places=2)
    image = models.ImageField(upload_to='proudcts/')

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(Customeuser,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
    

class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending','Pending'),
        ('Processing','Processing'),
        ('Delivered','Delivered'),
        ('Cancelled','Cancelled'),

    )

    user = models.ForeignKey(Customeuser,on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    price = models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
    
class Booking(models.Model):
    user = models.ForeignKey(Customeuser,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date}"    
    
class Review(models.Model):
    user = models.ForeignKey(Customeuser,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} - {self.rating}"   



