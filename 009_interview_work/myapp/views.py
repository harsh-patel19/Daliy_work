from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *

# Create your views here.

def product_list(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        qty = request.POST.get("qty")

        Product.objects.create(name=name,price=price,qty=qty)
        return redirect("product_list")
    
    Products =Product.objects.all()
    return render(request,"product_list.html",{"Products":Products})



def product_update(request,id):
    Products = get_object_or_404(Product,id=id)

    if request.method == "POST":
        Products.name = request.POST.get("name")
        Products.price = request.POST.get("price")
        Products.qty = request.POST.get("qty")

        Products.save()
        return redirect("product_list")
    
    return render(request,"product_update.html",{"Products":Products})


def product_delete(request,id):
    Products = get_object_or_404(Product,id=id)
    Products.delete()
    return redirect("product_list")