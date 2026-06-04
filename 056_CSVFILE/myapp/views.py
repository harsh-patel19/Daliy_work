from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *

# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        dept = request.POST.get("dept")
        salary = request.POST.get("salary")

        Employee.objects.create(name=name,dept=dept,salary=salary)
        return redirect("home")
    
    Employees = Employee.objects.all()
    return render(request,"home.html",{"Employees":Employees})


def update(request,id):
    Employees = Employee.objects.get(id=id)
    if request.method == "POST":
        Employees.name = request.POST.get("name")
        Employees.dept = request.POST.get("dept")
        Employees.salary = request.POST.get("salary")
        Employees.save()

        return redirect("home")
    
    return render(request,"update.html")

def user_delete(request,id):
    Employees = Employee.objects.get(id=id)
    Employees.delete()
    return redirect("home")