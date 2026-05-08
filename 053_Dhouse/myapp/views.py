from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
from myapp.serializers import *
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def user_regitser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        User.objects.create_user(
            username=username,
            password=password
        )
        return redirect("login")
    
    return render(request,"register.html")




def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        users = authenticate(

            username=username,
            password=password
        )
        if users is not None:
            login(request,users)
            return redirect("index")
        else:
            return render(request,"login.html")
        
    return render(request,"login.html")



def user_index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")

        Student.objects.create(name=name,email=email,phone_number=phone_number)
        return redirect("index")
    
    students = Student.objects.all()
    return render(request,"index.html",{"students":students})


def user_update(request,id):
    students = Student.objects.get(id=id)
    if request.method == "POST":
        students.name = request.POST.get("name")
        students.email = request.POST.get("email")
        students.phone_number = request.POST.get("phone_number")
        students.save()
        return redirect("index")
    return render(request,"update.html",{"students":students})

def user_delete(request,id):
    students = Student.objects.get(id=id)
    students.delete()
    return redirect("index")


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
        

class Studentdeatils(APIView):

    def get(self, request, id):
        Students = Student.objects.get(id=id)
        ser = StudentSerializer(Students)
        return Response(ser.data)

    def put(self, request, id):
        Students = Student.objects.get(id=id)
        ser = StudentSerializer(Students, data=request.data)

        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        else:
            return Response(ser.errors)

    def delete(self, request, id):
        Students = Student.objects.get(id=id)
        Students.delete()
        return Response("deleted")