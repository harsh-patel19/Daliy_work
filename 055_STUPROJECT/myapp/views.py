from django.shortcuts import render, redirect

from .models import Student

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse


@login_required
def home(request):

    search = request.GET.get('search')

    students = Student.objects.all()

    if search:

        students = students.filter(name__icontains=search)

    login_user = Student.objects.filter(user=request.user).first()

    if request.method == "POST":

        if login_user.role != 'admin':

            return HttpResponse('Only Admin Can Add Student')

        name = request.POST.get('name')

        email = request.POST.get('email')

        age = request.POST.get('age')

        role = request.POST.get('role')

        image = request.FILES.get('image')

        Student.objects.create(

            user=request.user,

            name=name,

            email=email,

            age=age,

            role=role,

            image=image

        )

        return redirect('home')

    return render(request, 'home.html', {

        'students': students

    })


def register(request):

    if request.method == "POST":

        username = request.POST.get('username')

        password = request.POST.get('password')

        name = request.POST.get('name')

        email = request.POST.get('email')

        age = request.POST.get('age')

        role = request.POST.get('role')

        image = request.FILES.get('image')

        user = User.objects.create_user(

            username=username,

            password=password

        )

        Student.objects.create(

            user=user,

            name=name,

            email=email,

            age=age,

            role=role,

            image=image

        )

        return redirect('login')

    return render(request, 'register.html')


def user_login(request):

    if request.method == "POST":

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(

            username=username,

            password=password

        )

        if user:

            login(request, user)

            return redirect('home')

    return render(request, 'login.html')


def user_logout(request):

    logout(request)

    return redirect('login')


@login_required
def update(request, id):

    login_user = Student.objects.filter(user=request.user).first()

    if login_user.role != 'admin':

        return HttpResponse('Only Admin Can Update')

    student = Student.objects.get(id=id)

    if request.method == "POST":

        student.name = request.POST.get('name')

        student.email = request.POST.get('email')

        student.age = request.POST.get('age')

        student.role = request.POST.get('role')

        if request.FILES.get('image'):

            student.image = request.FILES.get('image')

        student.save()

        return redirect('home')

    return render(request, 'update.html', {

        'student': student

    })


@login_required
def delete(request, id):

    login_user = Student.objects.get(user=request.user)

    if login_user.role != 'admin':

        return HttpResponse('Only Admin Can Delete')

    student = Student.objects.get(id=id)

    student.delete()

    return redirect('home')