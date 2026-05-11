from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from myapp.serializers import *

# Create your views here.

def user_register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        User.objects.create_user(username=username,password=password)
        return redirect("login")
    
    return render(request,"register.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        users = authenticate(

            username = username,
            password = password
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
        age = request.POST.get("age")

        Student.objects.create(name=name,email=email,age=age)
        return redirect("index")
    
    students = Student.objects.all()


    return render(request,"index.html",{"students":students})

def user_update(request,id):
    students = Student.objects.get(id=id)
    if request.method == "POST":
        students.name = request.POST.get("name")
        students.email = request.POST.get("email")
        students.age = request.POST.get("age")
        students.save()
        return redirect("index")
    
    return render(request,"update.html",{"students":students})

def user_delete(request,id):
    students = Student.objects.get(id=id)
    students.delete()
    return redirect("index")



######################## API ######################

@api_view(['GET'])
def get(request):
    students = Student.objects.all()
    ser = StudentSerializer(students,many=True)
    return Response(ser.data)

@api_view(['POST'])
def post(request):
    ser = StudentSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data)
    else:
        return Response(ser.errors)

@api_view(['PUT'])
def put(request,id):
    students = Student.objects.get(id=id)
    ser = StudentSerializer(students,data=request.data)
    if ser.is_valid():
        return Response(ser.data)
    else:
        return Response(ser.errors)
    
@api_view(['DELETE'])
def delete(request,id):
    students = Student.objects.get(id=id)
    students.delete()
    return redirect("data deleted succesfully")


class studentdeatils(APIView):
    def get(self,request):
        students = Student.objects.all()
        ser = StudentSerializer(students,many=True)
        return Response(ser.data)
    
    def post(self,request):
        ser = StudentSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
    

class Studentallview(APIView):
    def get(self,request,id):
        students = Student.objects.get(id=id)
        ser = StudentSerializer(students)
        return Response(ser.data)
    
    def put(self,request,id):
        students = Student.objects.get(id=id)
        ser = StudentSerializer(students,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response

