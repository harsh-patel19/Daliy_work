from django.shortcuts import render
from Myapp.models import *
from Myapp.serializers import *
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class StudentViweset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

