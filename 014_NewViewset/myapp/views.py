from django.shortcuts import render

# Create your views here.
# views.py

from rest_framework.viewsets import ModelViewSet
from myapp.models import *
from myapp.serializers import *

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


