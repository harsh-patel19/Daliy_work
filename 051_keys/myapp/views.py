from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    if request.method == "POST":
        category_id = request.POST.get("category")
        name = request.POST.get("name")
        decrib = request.POST.get("decrib")
        price = request.POST.get("price")
        qty = request.POST.get("qty")
        image = request.FILES.get("image")

        category = Category.objects.get(id=category_id)
        Product.objects.create(
            category=category,
            name=name,
            decrib=decrib,
            price=price,
            qty=qty,
            image = image
        )
        return redirect("home")
    
    category = Category.objects.all()
    products = Product.objects.all()

    search = request.GET.get("search")
    price = request.GET.get("price")
    if search:
        products = Product.objects.filter(name=search)

    if price:
        products = Product.objects.filter(price=price)

    paginator = Paginator(products,3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request,"home.html",{"products":products,"category":category,"page_obj":page_obj})

def update(request,id):
    products = Product.objects.get(id=id)
    category = Category.objects.all()
    if request.method == "POST":
        products.category_id = request.POST.get("category")
        products.name = request.POST.get("name")
        products.decrib = request.POST.get("decrib")
        products.price = request.POST.get("price")
        products.qty = request.POST.get("qty")

        if request.FILES.get("image"):
            products.image = request.FILES.get("image")
        products.save()
        return redirect("home")
    
    return render(request,"update.html",{"products":products,"category":category})

def user_delete(request,id):
    products = Product.objects.get(id=id)
    products.delete()
    return redirect("home")
