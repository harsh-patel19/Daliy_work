from django.shortcuts import render,redirect,get_object_or_404
from Myapp.models import *
from rest_framework.decorators import APIView
from rest_framework.response import Response
from Myapp.serializers import *

# Create your views here.
def employees_list(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        department = request.POST.get("department")
        salary = request.POST.get("salary")
        profile = request.FILES.get("profile")

        Employee.objects.create(name=name, email=email, department=department, salary=salary, profile=profile)
        return redirect("employees_list")
    
    Employees = Employee.objects.all()
    return render(request,"employees_list.html",{"Employees":Employees})


def employee_update(request,id):

    Employees = Employee.objects.get(id=id)
    if request.method == "POST":
        Employees.name = request.POST.get("name")
        Employees.email = request.POST.get("email")
        Employees.department = request.POST.get("department")
        Employees.salary = request.POST.get("salary")

        if request.FILES.get("profile"):
            Employees.profile = request.FILES.get("profile")
        
        Employees.save()
        return redirect("employees_list")
    
    return render(request,"employee_update.html",{"Employees":Employees})


def employee_delete(request,id):

    Employees = Employee.objects.get(id=id)
    Employees.delete()
    return redirect("employees_list")





# ------------------------------- APIView -------------------------------------

class Employeeslist(APIView):

    def get(self,request):
        Employees = Employee.objects.all()
        serializers = EmployeeSerializer(Employees,many=True)
        return Response(serializers.data)
    
    def post(self,request):
        serializers = EmployeeSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        
        return Response(serializers.errors)
    

class EmployeesDeatils(APIView):

    def get(self,request,id):
        Employees = Employee.objects.get(id=id)
        serializers = EmployeeSerializer(Employees)
        return Response(serializers.data)
    
    def put(self,request,id):
        Employees = Employee.objects.get(id=id)
        serializers = EmployeeSerializer(Employees,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return  Response(serializers.errors)
    
    def delete(self,request,id):
        Employees = Employee.objects.get(id=id)
        Employees.delete()
        return Response("deleted")