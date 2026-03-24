from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import *

def student_list(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        image = request.FILES.get("image")

        Student.objects.create(name=name, email=email, age=age, image=image)
        return redirect("student_list")

    Students = Student.objects.all()
    return render(request, "student_list.html", {"Students": Students})


def student_update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.age = request.POST.get("age")

        if request.FILES.get("image"):
            student.image = request.FILES.get("image")

        student.save()
        return redirect("student_list")

    return render(request, "student_update.html", {"student": student})


def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect("student_list")