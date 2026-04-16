from django.shortcuts import render
from rest_framework.decorators import APIView
from Myapp.serializers import *
from Myapp.models import*
from rest_framework.response import Response

# Create your views here.

class StudentApi(APIView):

    def get(self,request):
        Students = Student.objects.all()
        serializers = StudentSerializer(Students,many=True)
        return Response(serializers.data)
    
    def post(self,request):
        serializers = StudentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    

    def put(self,request,id):
        Students = Student.objects.get(id=id)
        serializers = StudentSerializer(Students,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    
    def delete(self,request,id):
        Students = Student.objects.get(id=id)
        Students.delete()
        return Response("deleted")