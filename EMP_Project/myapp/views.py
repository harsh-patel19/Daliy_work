from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.serializers import *
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
        if users is not None:
            login(request,users)
            return redirect("home")
    
    return render(request,"login.html")


def user_logout(request):
    logout(request)
    return redirect('login')



def home(request):
    search = request.GET.get('search')

    employees = Employee.objects.all().order_by('-id')

    if search:
        employees = employees.filter(name__icontains=search)

    paginator = Paginator(employees,3)
    page_number = request.GET.get('page')
    employees =paginator.get_page(page_number)

    return render(request,"home.html",{"employees":employees})


@login_required
def add_employee(request):
    
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        role = request.POST.get("role")
        image = request.FILES.get("image")

        Employee.objects.create(
            user = request.user,
            name=name,
            email=email,
            age=age,
            role=role,
            image=image
        )
        return redirect("home")
    
    return render(request,"add_employee.html")


@login_required
def update_employee(request,id):

    employee = Employee.objects.get(id=id)

    if request.method == "POST":
        employee.name = request.POST.get("name")
        employee.email = request.POST.get("email")
        employee.age = request.POST.get("age")
        employee.role = request.POST.get("role")

        if request.FILES.get("image"):
            employee.image = request.FILES.get("image")

            employee.save()
            return redirect("home")
        
    return render(request,"update.html",{"employee":employee})
    

@login_required
def delete_employee(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("home")



@api_view(['GET'])
def employee_api(request):
    employee = Employee.objects.all()
    ser = EmployeeSerializer(employee,many=True)
    return Response(ser.data)


@login_required
def admin_page(request):
    employee = Employee.objects.get(user=request.user)
    if employee.role != 'admin':
        return HttpResponse("access denied")
    return HttpResponse('WElcome admin')

