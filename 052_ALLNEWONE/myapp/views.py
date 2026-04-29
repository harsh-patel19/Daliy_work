from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator
# Create your views here

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

        if users is not None:
            login(request,users)
            return redirect("home")
        else:
            return render(request,"login.html")
        
    return render(request,"login.html")


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        qty = request.POST.get("qty")
        manudate = request.POST.get("manudate")
        enddate = request.POST.get("enddate")
        image = request.FILES.get("image")

        Product.objects.create(name=name,price=price,qty=qty,manudate=manudate,enddate=enddate,image=image)
        return redirect("home")
    
    products = Product.objects.all()

    search  = request.GET.get("search")
    price = request.GET.get("price")
    if search:
        products = products.filter(name=search)

    if price:
        products = products.filter(price=price)

    Paginators = Paginator(products,2)
    page_number = request.GET.get('page')
    products =Paginators.get_page(page_number)

    return render(request,"home.html",{"products":products})


def user_update(request,id):
    products = Product.objects.get(id=id)
    if request.method == "POST":
        products.name = request.POST.get("name")
        products.price = request.POST.get("price")
        products.qty = request.POST.get("qty")
        products.manudate = request.POST.get("manudate")
        products.enddate = request.POST.get("enddate")

        if request.FILES.get("image"):
            products.image = request.FILES.get("image")

        products.save()
        return redirect("home")
    
    return render(request,"update.html",{"products":products})


def user_delete(request,id):
    products = Product.objects.get(id=id)
    products.delete()
    return redirect("home")

