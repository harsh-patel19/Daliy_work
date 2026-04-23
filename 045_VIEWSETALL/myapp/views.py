from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from myapp.models import *
from myapp.serializers import *

# Create your views here.

class Studentviewset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerailizer

    permission_classes = [IsAuthenticated]

    filter_backends =[DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ["name","email","dept"]
    search_fields = ["name","dept"]

    ordering_fields =["email"]