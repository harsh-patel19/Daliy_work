from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
from rest_framework.decorators import APIView
from rest_framework.response import Response
from myapp.serializers import *


class Studentlist(APIView):

    def get(self,request):
        Students = Student.objects.all()
        ser = StudentSerializer(Students,many=True)
        return Response(ser.data)

    def post(self,request):
        ser = StudentSerializer(data=request.data)
        
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        else:
            return Response(ser.errors)
        
    
class Studentdetails(APIView):

    def get(self,request,id):
        Students = Student.objects.get(id=id)
        ser = StudentSerializer(Students)
        return Response(ser.data)
    
    def put(self,request,id):
        Students = Student.objects.get(id=id)
        ser = StudentSerializer(Students,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        
        return Response(ser.errors)
    
    def delete(self,request,id):
        Students = Student.objects.get(id=id)
        Students.delete()
        return Response("deleted")
    
    