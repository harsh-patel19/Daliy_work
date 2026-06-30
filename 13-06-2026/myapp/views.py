from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

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
        email = request.POST.get("email")
        age = request.POST.get("age")
        image = request.FILES.get("image")

        Student.objects.create(
            name=name,
            email=email,
            age=age,
            image=image
        )
        return redirect("home")
    students = Student.objects.all()
    return render(request,"home.html",{"students":students})




def user_update(request,id):
    students = Student.objects.get(id=id)
    if request.method == "POST":
        students.name = request.POST.get("name")
        students.email = request.POST.get("email")
        students.age = request.POST.get("age")

        if request.FILES.get("image"):
            students.image = request.FILES.get("image")

        return redirect("home")
    
    return render(request,"update.html")

def user_delete(request,id):
    students = Student.objects.get(id=id)
    students.delete()
    return redirect("home")