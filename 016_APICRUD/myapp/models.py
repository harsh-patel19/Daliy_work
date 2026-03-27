from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.name
    

class Coruse(models.Model):
    name = models.CharField(max_length=100)
    email = models.ForeignKey(Student,on_delete=models.CASCADE)
    age = models.IntegerField()