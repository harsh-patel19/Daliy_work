from django.shortcuts import render,redirect
from myapp.models import *


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            students = Student.objects.get(username=username, password=password)
            request.session['username'] = students.username
            return redirect("home")
        except Student.DoesNotExist:
            return render(request,"login.html",{"user not found"})
    return render(request,"login.html")
            
def home(request):
    username = request.session.get("username")
    if username is None:
        return render(request,"login.html")
    return render(request,"home.html")

def logout(request):
    request.session.flush()
    return redirect("login")