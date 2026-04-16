from django.shortcuts import render
from rest_framework.decorators import api_view,APIView,permission_classes
from rest_framework.response import Response
from Myapp.models import *
from Myapp.serializers import *
from rest_framework.permissions import IsAuthenticated,AllowAny

# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def get(request):
    students = student.objects.all()
    serializers = StudentSerializer(students,many=True)
    return Response(serializers.data)

@permission_classes([IsAuthenticated])
@api_view(['POST'])
def post(request):
    serializers = StudentSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    return Response(serializers.errors)

@api_view(['PUT'])
def put(request,id):
    students = student.objects.get(id=id)
    serializers = StudentSerializer(students,data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    return Response(serializers.errors)
    
@api_view(['PATCH'])
def patch(request,id):
    students = student.objects.get(id=id)
    serializers = StudentSerializer(students,data=request.data,partial=True)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    return Response(serializers.errors)
    
@api_view(['DELETE'])
def delete(request,id):
    students = student.objects.get(id=id)
    students.delete()
    return Response("deleted")


class studentview(APIView):

    def get(self,request):
        students = student.objects.all()
        serializers = StudentSerializer(students,many=True)
        return Response(serializers.data)
    
    def post(self,request):
        serializers = StudentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    

class Studentdetails(APIView):

    def get(self,request,id):
        students = student.objects.get(id=id)
        serializers = StudentSerializer(students)
        return Response(serializers.data)
    
    def put(self,request,id):
        students = student.objects.get(id=id)
        serializers = StudentSerializer(students,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    
    def patch(self,request,id):
        students = student.objects.get(id=id)
        serializers = StudentSerializer(students,data=request.data,partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

    
    def delete(self,request,id):
        students = student.objects.get(id=id)
        students.delete()
        return Response({"messgae":"deleted data..."})