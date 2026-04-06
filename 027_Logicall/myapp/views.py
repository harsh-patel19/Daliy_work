from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
from rest_framework.decorators import APIView
from rest_framework.response import Response
from myapp.serializers import *

# Create your views here.
def student_list(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        image = request.FILES.get("image")

        Student.objects.create(name=name, email=email, age=age, image=image)
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
            Students.image = request.FILES.get("image")

        Students.save()

        return redirect("student_list")
    
    return render(request,"student_update.html",{"Students":Students})



def student_delete(request,id):
    Students = Student.objects.get(id=id)
    Students.delete()
    return redirect("student_list")


class Studentview(APIView):

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
        ser = StudentSerializer(Students,data= request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        else:
            return Response(ser.errors)
        
    
    def delete(self,request,id):
        Students = Student.objects.get(id=id)
        Students.delete()
        return Response("deleted")