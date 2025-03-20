from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Item
from django.contrib import messages

# Create your views here.
def add_product(request):
    if request.method == 'POST':
        prod = Item()
        prod.name = request.POST['name']
        prod.price = request.POST['price']
        prod.description = request.POST['description']

        if len(request.FILES) != 0:
            prod.image = request.FILES['image']
        prod.save()
        messages.success(request, 'Product added successfully')
        return redirect('view_products')
    return render(request, 'add_product.html')

def view_products(request):
    products = Item.objects.all()
    return render(request, 'view_products.html', {'products': products})