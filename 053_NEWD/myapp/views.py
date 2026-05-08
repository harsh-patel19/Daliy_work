from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from rest_framework.decorators import APIView
from rest_framework.response import Response
from myapp.serializers import *
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
        price = request.POST.get("price")
        qty = request.POST.get("qty")
        image = request.FILES.get("image")
        dec = request.POST.get("dec")

        Product.objects.create(name=name,price=price,qty=qty,image=image,dec=dec)
        return redirect("index")
    
    products = Product.objects.all()
    return render(request,"index.html",{"products":products})
  

def user_update(request,id):
    products = Product.objects.get(id=id)
    if request.method == "POST":
        products.name = request.POST.get("name")
        products.price = request.POST.get("price")
        products.qty = request.POST.get("qty")
        
        if request.FILES.get("image"):
            products.image = request.FILES.get("image")
        products.save()

        return redirect("index")
    
    return render(request,"update.html",{"products":products})

def user_delete(request,id):
    products = Product.objects.get(id=id)
    products.delete()
    return redirect("index")


class productview(APIView):

    def get(self,request):
        products = Product.objects.all()
        ser = ProductSerializer(products,many=True)
        return Response(ser.data)
    

    def post(self,request):
        ser = ProductSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        
        return Response(ser.errors)


class productdeatils(APIView):

    def get(self,request,id):
        products = Product.objects.get(id=id)
        ser = ProductSerializer(products)
        return Response(ser.data)
    
    def put(self,request,id):
        products = Product.objects.get(id=id)
        ser = ProductSerializer(products,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
    
    def delete(self,request,id):

        products = Product.objects.get(id=id)
        products.delete()
        return Response("deleted successfully data")
    