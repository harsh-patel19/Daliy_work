from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from myapp.serializers import *

# Create your views here.

def student_list(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        phone = request.POST.get("phone")
        image = request.FILES.get("image")

        Student.objects.create(name=name, email=email, age=age, phone=phone, image=image)
        return redirect("student_list")
    
    Students = Student.objects.all()
    return render(request,"student_list.html",{"Students":Students})


def student_update(request,id):
    Students = get_object_or_404(Student,id=id)

    if request.method == "POST":
        Students.name = request.POST.get("name")
        Students.email = request.POST.get("email")
        Students.age = request.POST.get("age")
        Students.phone = request.POST.get("phone")

        if request.FILES.get("image"):
            Students.image = request.FILES.get("image")
        Students.save()

        return redirect("student_list")
    
    return render(request,"student_update.html",{"Students":Students})

def student_delete(request,id):
    Students = get_object_or_404(Student,id=id)
    Students.delete()
    return redirect("student_list")
        

# ________________________________________________________________________________________________________

class StudentList(APIView):
    def get(self,request):
        Students = Student.objects.all()
        serializer = StudentSerializer(Students,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.data)
    



class StudentDetails(APIView):

    def get(self,request,pk):
        Students = Student.objects.get(pk=pk)
        serializers = StudentSerializer(Students)
        return Response(serializers.data)
  


    def put(self,request,pk):
        Students = Student.objects.get(pk=pk)
        serializers = StudentSerializer(Students,data= request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        
        return Response(serializers.errors)
    
    def delete(self,request,pk):
        Students = Student.objects.get(pk=pk)
        Students.delete()
        return Response("deleted")