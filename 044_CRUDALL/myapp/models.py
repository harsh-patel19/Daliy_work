from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(150)
    dept = models.CharField(50)
    salary = models.IntegerField()
    profile = models.ImageField(upload_to='profiles/',null=True,blank=True)

    