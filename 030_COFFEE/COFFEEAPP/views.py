from django.shortcuts import render,redirect,get_object_or_404
from COFFEEAPP.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def regiter(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password = request.POST.get("Password")

        user = Customeuser.objects.create_user(
            full_name = full_name,
            email= email,
            password=password
        )
        return redirect("login")
    
    return render(request,"register.html",{"user":user})


def user_login(request):
    if request.method == "POST":
        email = request.POSt.get("email"),
        password = request.POST.get("password"),

        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect("index")
        else:
            return render(request,"login.html")
        
    return render(request,"login.html")



def index(request):
    products = Product.objects.all()
    return render(request,"index.html",{"products":products})


def about(request):
    return render(request,"about.html")

def admin(request):
    return render(request,"admin.html")

def booking(request):
    return render(request,"booking.html")


def cart(request):
    return render(request,"cart.html")

def add_to_cart(request,id):
    product = get_object_or_404(Product,id=id)

    cart_item, created = Cart.objects.all(user=request.user,product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("menu")


def view_cart(request):
    cart_item = Cart.objects.filter(user=request.user)
    total = 0

    for item in cart_item:
        total += item.total_price()

    return render(request,"cart.html")

def chatbot(request):
    return render(request,"chatbot.html")

def contact(request):
    return render(request,"contact.html")


def login(request):
    return render(request,"login.html")


def menu(request):
    products = Product.objects.all()
    return render(request,"menu.html",{"products":products})



def order(request):
    return render(request,"order.html")

def reviews(request):
    return render(request,"reviews.html")

def suggestions(request):
    return render(request,"suggestions.html")
