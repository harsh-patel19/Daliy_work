from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# LIST + SEARCH + FILTER
def product_list(request):
    products = Product.objects.all()

    # Search
    search = request.POST.get('search')
    if search:
        products = products.filter(name__icontains=search)

    # Filter
    category = request.POST.get('category')
    if category:
        products = products.filter(category=category)

    return redirect("product_list")


# CREATE
def product_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category = request.POST.get('category')

        Product.objects.create(
            name=name,
            description=description,
            price=price,
            category=category
        )
        return redirect('product_list')

    return render(request, 'product_create.html')


# UPDATE
def product_update(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.category = request.POST.get('category')
        product.save()

        return redirect('product_list')

    return render(request, 'product_update.html', {'product': product})


# DELETE
def product_delete(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        product.delete()
        return redirect('product_list')

    return render(request, 'product_delete.html', {'product': product})