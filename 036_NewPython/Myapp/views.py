from django.shortcuts import render,redirect,get_object_or_404
from Myapp.models import *

# Create your views here.


def index(request):
    if request.method =="POST":
        Category_id = request.POST.get('category')
        name = request.POST.get("name")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        image = request.FILES.get("image")

        category = Category.objects.get(id=Category_id)
        
        Product.objects.create(category=category,name=name,price=price,quantity=quantity,image=image)
        return redirect("index")
    
    Categorys = Category.objects.all()
    products = Product.objects.all()
    return render(request,"index.html",{"Categorys":Categorys,"products":products})


