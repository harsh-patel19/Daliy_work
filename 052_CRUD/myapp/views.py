from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator
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

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:
            login(request,user)
            return redirect("student_list")
        else:
            return render(request,"login.html")
        
    return render(request,"register.html")

def user_logout(request):
    logout(request)
    return redirect("login")

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        birth_of_date = request.POST.get("birth_of_date")
        image = request.FILES.get("image")

        Student.objects.create(name=name,email=email,birth_of_date=birth_of_date,image=image)
        return redirect("student_list")
    
    students = Student.objects.all()

    serach = request.GET.get("search")
    if serach:
        students = students.filter(name=serach)

    paginator = Paginator(students,2)
    page_number = request.GET.get("page")
    students = paginator.get_page(page_number)


    
    return render(request,"student_list.html",{"students":students})


def user_update(request,id):
    students = Student.objects.get(id=id)
    if request.method == "POST":
        students.name = request.POST.get("name")
        students.email = request.POST.get("email")
        students.birth_of_date = request.POST.get("birth_of_date")

        if request.FILES.get("image"):
            students.image = request.FILES.get("image")
        students.save()
        return redirect("student_list")
    
    return render(request,"update.html",{"students":students})

def user_delete(request,id):
    students = Student.objects.get(id=id)
    students.delete()
    return redirect("student_list")