from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# from rest_framework.decorators import api_view,APIView
# from rest_framework.response import Response
# from myapp.serializers import *
# Create your views here.
def user_reg(request):
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
        dec = request.POST.get("dec")
        image = request.FILES.get("image")

        Product.objects.create(name=name,qty=qty,price=price,dec=dec,image=image)
        return redirect("home")
    
    products = Product.objects.all()
    return render(request,"home.html",{"products":products})

def user_update(request,id):
    products = Product.objects.get(id=id)
    if request.method == "POST":

        products.name =request.POST.get("name")
        products.qty =request.POST.get("qty")
        products.price =request.POST.get("price")
        products.dec =request.POST.get("dec")

        if request.FILES.get("image"):
            products.image = request.FILES.get("image")
            
        products.save()
        return redirect("home")
    
    return render(request,"update.html",{"products":products})


def user_delete(request,id):
    products = Product.objects.get(id=id)
    products.delete()
    return redirect("home")



# 
#   API 
# 

# class productdeatils(APIView):
#     def get(self,request):
#       Products = Product.objects.all()
#       ser = productserializer(Products,many=True)
#       return Response(ser.data)
    
#     def post(self,request):
#        ser = productserializer(data=request.data)
#        if ser.is_valid():
#           ser.save()
#           return Response(ser.data)
       
#        return Response(ser.errors)
    

# class Productall(APIView):
#     def get(self,request,id):
#         Products = Product.objects.get(id=id)
#         ser = productserializer(Products)
#         return Response(ser.data)

#     def put(self,request,id):
#        Products = Product.objects.get(id=id)
#        ser = productserializer(Products,data=request.data)
#        if ser.is_valid():
#           ser.save()
#           return Response(ser.data)
       
#        return Response(ser.errors)



