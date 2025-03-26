from django.contrib import messages
from django.shortcuts import render, redirect
from owner.models import Product, ProductImage


def landingpage(request):
    return render(request, 'landingpage.html')


def display_products(request):
    products = Product.objects.all()
    return render(request, 'display_products.html', {'products': products})

def product_details(request,  product_id):
    product = Product.objects.get(id=product_id)
    images = ProductImage.objects.filter(product=product)
    return render(request, 'product_details.html', {'product': product, 'images': images})


def product_payment(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_payment.html', {'product': product})
    