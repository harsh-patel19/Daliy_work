from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        User.objects.create_user(
            username =username,
            password = password
        )
        return redirect("login")
    
    return render(request,"register.html")



def user_login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request=request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("product_list")
        else:
            return render(request,"login.html",{"error":"Invalid Username or Password"})

    return render(request,"login.html")
def user_logout(request):
    logout(request)
    return redirect("login")

def product_list(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        photo = request.FILES.get("photo")

        Product.objects.create(
            name=name,
            age=age,
            photo=photo
        )

        return redirect("product_list")

    Products = Product.objects.all()
    return render(request,"product_list.html",{"Products":Products})


def product_update(request, id):
    Products = get_object_or_404(Product, id=id)

    if request.method == "POST":
        Products.name = request.POST.get("name")
        Products.age = request.POST.get("age")

        if request.FILES.get("photo"):
            Products.photo = request.FILES.get("photo")

        Products.save()
        return redirect("product_list")

    return render(request,"product_update.html",{"Products":Products})


def product_delete(request,id):
    Products = get_object_or_404(Product,id=id)
    Products.delete()
    return redirect("product_list")