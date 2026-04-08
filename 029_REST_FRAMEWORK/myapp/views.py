from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from myapp.models import *
from myapp.serializers import *
# Create your views here.

class Studentview(APIView):

    def get(self,request):
        Students = Student.objects.all()
        serializers = StudentSeializer(Students,many=True)
        return  Response(serializers.data)
    
    def post(self,request):
        serializers = StudentSeializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        
        return Response(serializers.errors)
    

class StudentDeatils(APIView):

    def get(self,request,id):
        Students = Student.objects.get(id=id)
        serializers = StudentSeializer(Students)
        return Response(serializers.data)
    
    def put(self,request,id):
        Students = Student.objects.get(id=id)
        serializers = StudentSeializer(Students,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    

    