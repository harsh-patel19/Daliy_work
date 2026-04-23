from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import Studentlist
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentlist

    permission_classes = [IsAuthenticated]

    filter_backends =[DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields =["age","name","email"]
    search_fields =["name","email"]
    Ordering_fields =["age"]
    