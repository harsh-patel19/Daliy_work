from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import Studentlist
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentlist

    filter_backends =[DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields =["age","name"]
    search_fields =["name"]
    Ordering_fields =["age"]
    