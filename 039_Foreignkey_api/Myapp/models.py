from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)


class Student(models.Model):
    name = models.CharField(max_length=100)
    profile = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    