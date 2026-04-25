from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
from django.core.paginator import Paginator
# Create your views here.
def product_list(request):
    products = Product.objects.all()

    search = request.GET.get('search')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if search:
        products = products.filter(name=search)

    if min_price:
        products = products.filter(price__gte=min_price)

    if max_price:
        products = products.filter(price__lte=max_price)

    paginator = Paginator(products, 5)  # 5 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'product_list.html', {'page_obj': page_obj})

def product_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')

        Product.objects.create(
            name=name,
            description=description,
            price=price
        )
        return redirect('product_list')

    return render(request, 'product_create.html')


def product_update(request,id):
    product = get_object_or_404(Product,id=id)

    if request.method == "POST":
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.save()

        return redirect("product_list")
    
    return render(request,"product_update.html",{"product":product})

def product_delete(request,id):
    product = get_object_or_404(Product,id=id)
    product.delete()
    return redirect("product_list")