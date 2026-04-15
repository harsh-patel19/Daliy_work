from django.shortcuts import render,redirect
from Myapp.models import *
from rest_framework.decorators import APIView
from rest_framework.response import Response
from Myapp.serializers import *
import os
# Create your views here.
def student_list(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        image = request.FILES.get("image")

        Student.objects.create(name=name,email=email,age=age,image=image)
        return redirect("student_list")
    
    Students = Student.objects.all()
    return render(request,"student_list.html",{"Students":Students})

def student_update(request,id):
    Students = Student.objects.get(id=id)
    if request.method == "POST":
        Students.name = request.POST.get("name")
        Students.email = request.POST.get("email")
        Students.age = request.POST.get("age")
        
        if request.FILES.get("image"):
            # Delete old image if exists
            if Students.image and os.path.isfile(Students.image.path):
                os.remove(Students.image.path)

            # Always assign new image (OUTSIDE delete block)
            Students.image = request.FILES["image"]
        Students.save()
        return redirect("student_list")
    
    return render(request,"student_update.html",{"Students":Students})
        

def student_delete(request,id):
    Students = Student.objects.get(id=id)
    Students.delete()
    if Students.image:
        os.remove(Students.image.path)
    return redirect("student_list")


class StudentDeatils(APIView):

    def get(self,request):
        Students = Student.objects.all()
        ser = StudentSerializer(Students,many=True)
        return Response(ser.data)
    
    def post(self,request):
        ser = StudentSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
    

class Studentlist(APIView):

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
    