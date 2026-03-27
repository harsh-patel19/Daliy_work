from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from myapp.serializers import *

from rest_framework import viewsets
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.viewsets import ModelViewSet
# Create your views here.

# class Studentlist(APIView):

#     def get(self,request):
#         Students = Student.objects.all()
#         ser = StudentSerializer(Students,many=True)
#         return Response(ser.data)
    
#     def post(self,request):
#         ser = StudentSerializer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         return Response(ser.errors)
    

# class StudenDeatils(APIView):

#     def get(self,request,id):
#         Students = Student.objects.get(id=id)
#         ser = StudentSerializer(Students)
#         return Response(ser.data)
    
#     def put(self,request,id):
#         Students = Student.objects.get(id=id)
#         ser = StudentSerializer(Students,data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         return Response(ser.errors)

#     def delete(self,request,id):
#         Students = Student.objects.get(id=id)
#         Students.delete()
#         return Response("deleted")
        

class studentviewset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class Courseviewset(ModelViewSet):
    queryset = Coruse.objects.all()
    serializer_class = CourseSerializer