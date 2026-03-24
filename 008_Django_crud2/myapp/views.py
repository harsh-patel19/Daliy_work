from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Student


def student_list(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")

        Student.objects.create(name=name, email=email, age=age)
        return redirect("student_list")
    
    Students = Student.objects.all()
    return render(request, "student_list.html", {"Students": Students})


def student_update(request, id):
    Students = get_object_or_404(Student, id=id)

    if request.method == "POST":
        Students.name = request.POST.get("name")
        Students.email = request.POST.get("email")
        Students.age = request.POST.get("age")

        Students.save()
        return redirect("student_list")
    
    return render(request, "student_update.html", {"Students": Students})


def student_delete(request, id):
    Students = get_object_or_404(Student, id=id)
    Students.delete()
    return redirect("student_list")