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
        login(request,users)
        return redirect("home")
    
    return render(request,"login.html")

def user_home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        qty = request.POST.get("qty")
        price = request.POST.get("price")
        image = request.FILES.get("image")

        Product.objects.create(name=name,qty=qty,price=price,image=image)
        return redirect("home")
    
    Products = Product.objects.all()
    return render(request,"home.html",{"Products":Products})

def user_update(request,id):
    Products = Product.objects.get(id=id)
    if request.method == "POST":
        Products.name = request.POST.get("name")
        Products.qty = request.POST.get("qty")
        Products.price = request.POST.get("price")

        if request.FILES.get("image"):
            Products.image = request.FILES.get("image")
            
        Products.save()
        return redirect("home")
    
    return render(request,"update.html",{"Products":Products})


def user_delete(request,id):
   Products = Product.objects.get(id=id)
   Products.delete()
   return redirect("home") 



class ProductDeatils(APIView):
    def get(self,request):
        Products = Product.objects.all()
        ser = ProductSerializers(Products,many=True)
        return Response(ser.data)


    def post(self,request):
        ser = ProductSerializers(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
    

class ProductDeatilsall(APIView):
    def get(self,request,id):
        Products = Product.objects.get(id=id)
        ser = ProductSerializers(Products)
        return Response(ser.data)
    

    def put(self,request,id):
        Products = Product.objects.get(id=id)
        ser = ProductSerializers(Products,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
    