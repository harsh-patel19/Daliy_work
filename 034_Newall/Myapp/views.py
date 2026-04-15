from django.shortcuts import render,redirect,get_object_or_404
from Myapp.models import *

# Create your views here.

def Employees_list(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        image = request.FILES.get("image")

        Employee.objects.create(name=name, email=email, age=age, image=image)
        return redirect("Employees_list")
    
    Employees = Employee.objects.all()
    return render(request,"Employees_list.html",{"Employees":Employees})


def Employees_update(request,id):
    Employees = Employee.objects.get(id=id)
    if request.method == "POST":
        Employees.name = request.POSt.get("name")
        Employees.email = request.POST.get("email")
        Employees.age = request.POST.get("age")
        

        if request.FILES.get("image"):
            Employees.image = request.FILES.get("image")

        Employees.save()
        return redirect("Employees_list")
    
    return render(request,"Employees_update.html",{"Employees":Employees})



def Employees_delete(request,id):
    Employees = Employee.objects.get(id=id)
    Employees.delete()
    return redirect("Employees_list")
