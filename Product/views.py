from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product
from .form import ProductCreateForm


# PRODUCT LIST
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        print(products)
    context = {
        "title": 'Product List',
        "products": products
    }
    return render(request, 'Product/product_list.html', context)


# PRODUCT DETAILS
def product_details(request, id=None):
    if request.method == 'GET':
        product = get_object_or_404(Product, pk=id)
    context = {
        "title": 'Product details',
        "product": product
    }
    return render(request, 'Product/product_details.html', context)


# PRODUCT CREATE
def product_create(request):
    if request.method == 'GET':
        form = ProductCreateForm()
    elif request.method == 'POST':
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.success(request, 'Product Created.')
            return redirect('product_list')
    context = {
        "title": 'Product create',
        "form": form
    }
    return render(request, 'Product/product_create.html', context)


# PRODUCT UPDATE
def product_update(request, id):
    obj = get_object_or_404(Product, pk=id)
    form = ProductCreateForm(request.POST or None, instance=obj)

    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.success(request, 'Post Updated.')
            return redirect('product_list')

    context = {
        "title": "Update blog",
        "form": form
    }
    return render(request, "Product/product_update.html", context)


# PRODUCT DELETE
def product_detete(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'GET':
        product.delete()
        messages.success(request, 'Product Deleted.')

    return redirect('product_list')
