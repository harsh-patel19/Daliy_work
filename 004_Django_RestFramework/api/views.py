from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from api.models import *
from api.serializers import *
# Create your views here.


@api_view(['GET'])
def student_list(request):
    Students = Student.objects.all()
    serializer = StudentSerializer(Students,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def student_list(request,id):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)




 
class StudentList(APIView):

    def get(self,request):
        Students = Student.objects.all()
        serializer = StudentSerializer(Students,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.data)
    


class StudentDetails(APIView):

    def get(self,request,pk):
        Students = Student.objects.get(pk=pk)
        serializer = StudentSerializer(Students)
        return Response(serializer.data)
    
    def put(self,request,pk):
        Students = Student.objects.get(pk=pk)
        serializer = StudentSerializer(Students,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def delete(self,request,pk):
        Students = get_object_or_404(Student,pk=pk)
        Students.delete()
        return Response("student deleted")







