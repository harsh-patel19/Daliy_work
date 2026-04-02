from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def student_list(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        image = request.FILES.get("image")
      
        Student.objects.create(user=request.user,name=name, email=email, age=age, image=image)
        return redirect("student_list")
    
    Students = Student.objects.filter(user=request.user)
    return render(request,"student_list.html",{"Students":Students})

def student_update(request,id):
    Students = Student.objects.get(id=id)
    if request.method == "POST":
        Students.name = request.POST.get("name")
        Students.email = request.POST.get("email")
        Students.age= request.POST.get("age")
        
        if request.FILES.get("image"):
            Students.image = request.FILES.get('image')

        Students.save()
        return redirect("student_list")
    return render(request,"student_update.html",{"Students":Students})

def student_delete(request,id):
    Students = Student.objects.get(id=id)
    Students.delete()
    return redirect("student_list")
       



def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        User.objects.create_user(username=username, password=password)
        return redirect('user_login')

    return render(request, 'register.html')


# 🔹 Login
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('student_list')
        else:
            return render(request, 'user_login.html', {'error': 'Invalid credentials'})

    return render(request, 'user_login.html')


# 🔹 Logout
def user_logout(request):
    logout(request)
    return redirect('user_login')
