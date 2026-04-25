from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from myapp.models import *
import os

# Create your views here.
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return redirect("login")
    
    return render(request,"register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request=request,
            username=username,
            password=password
        )

        if user is not None:
            login(request,user)
            return redirect("list")
        else:
            return render(request,"login.html")
        

    return render(request,"login.html")

def logout_view(request):
    logout(request)
    return redirect("register")

@login_required
def student_list(request):
    students = Student.objects.all()

    search = request.GET.get("search")
    if search:
        students = students.filter(name=search)
    
    course = request.GET.get("course")
    if course:
        students = students.filter(course=course)
    return render(request,"list.html",{"students":students})

@login_required
def student_create(request):
    if request.method == "POST":
        Student.objects.create(
            name = request.POST.get("name"),
            email = request.POST.get("email"),
            age = request.POST.get("age"),
            course = request.POST.get("course"),
            image=request.FILES.get("image")

        )
        return redirect("list")

    return render(request,"create.html")

@login_required
def student_update(request,id):
    students = get_object_or_404(Student,id=id)

    if request.method == "POST":
        students.name = request.POST.get("name")
        students.email = request.POST.get('email')
        students.age = request.POST.get('age')
        students.course = request.POST.get('course')

        if request.FILES.get("image"):
            if students.image.path:
                os.remove(students.image.path)
            students.image = request.FILES.get("image")
        students.save()
        return redirect("list")
    
    return render(request,"update.html",{"students":students})


@login_required
def student_delete(request,id):
    students = get_object_or_404(Student,id=id)
    if students.image.path:
        os.remove(students.image.path)
    students.delete()
    return redirect("list")
