from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *

# Create your views here.
def Employees_list(request):
    if request.method =="post":
        name = request.post.get("name")
        dept = request.post.get("dept")
        salary = request.post.get("salary")
        profile = request.FIELS.get("profile")

        Employee.objects.create(name=name, dept=dept, salary=salary, profile=profile)
        return redirect("Employees_list")
    
    Employees = Employee.objects.all()
    return render(request,"Employees_list.html",{"Employees":Employees})


def Employees_update(request,id):
    Employees = Employee.objects.get(id=id)
    if request.method =="post":
        Employees.name = request.post.get("name")
        Employees.dept = request.post.get("dept")
        Employees.salary = request.post.get("salary")
        
        if request.FILES.get("profile"):
            Employees.profile = request.FILES.get("profile")

        Employees.save()
        return redirect("Employees_list")
    
    return render(request,"Employees_update.html",{"Employees":Employees})

def Employees_delete(request,id):
    Employees = Employee.objects.get(id=id)
    Employees.delete()
    return redirect("Employees_list")