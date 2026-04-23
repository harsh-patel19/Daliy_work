from django.shortcuts import render,redirect
from myapp.models import*


# Create your views here.
def product_list(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        image = request.FILES.get("image")

        Product.objects.create(name=name, email=email, age=age, image=image)
        return redirect("product_list")
    
    Products = Product.objects.all()
    return render(request,"product_list.html",{"Products":Products})


def product_update(request,id):
    Products = Product.objects.get(id=id)
    if request.method =="POST":
        Products.name = request.POST.get("name")
        Products.email = request.POST.get("email")
        Products.age = request.POST.get("age")

        if request.FILES.get("image"):
            Products.image = request.FILES.get("image")
        Products.save()

        return redirect("product_list")
    
    return render(request,"product_update.html",{"Products":Products})

def product_delete(request,id):
    Products = Product.objects.get(id=id)
    Products.delete()
    return redirect("product_list")