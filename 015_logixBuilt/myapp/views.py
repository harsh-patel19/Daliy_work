from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from myapp.serializers import *
from myapp.models import *
from rest_framework import status

# Create your views here.

@api_view(['GET','POST'])
def student_list(request):
    if request.method == "GET":
        Students = Student.objects.all()
        ser = StudentSerializer(Students,many=True)
        return Response(ser.data)
    
    elif request.method == "POST":
        ser = StudentSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
    
# BYID

@api_view(['GET', 'PUT', 'DELETE'])
def student_deatils(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    # GET
    if request.method == "GET":
        ser = StudentSerializer(student)
        return Response(ser.data)

    # PUT (UPDATE)
    elif request.method == "PUT":
        ser = StudentSerializer(student, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)  # ✅ FIXED
        return Response(ser.errors, status=400)

    # DELETE
    elif request.method == "DELETE":
        student.delete()
        return Response({"message": "Deleted"}, status=204)