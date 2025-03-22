from django.shortcuts import render, redirect
from .forms import OwnerCreationForm, OwnerLoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login   
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth import logout
from .models import Product

def homepage(requst):
    return render(requst, 'homepage.html')

@csrf_protect
def owner_singup(request):
    if request.method == 'POST':
        form = OwnerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('owner_login')
        else:
            messages.error(request, 'Invalid information')   
    else:
        form = OwnerCreationForm()
    return render(request, 'owner_singup.html', {'form': form})

@csrf_protect
def owner_login(request):
    if request.method == 'POST':
        form = OwnerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password =form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You are now logged in successfully')
                return redirect('owner_dashboard')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = OwnerLoginForm()
    context = {
        'form': form,
    }
    return render(request, 'owner_login.html', context)

def owner_logout(request):
    logout(request)
    messages.success(request, 'You are now logged out')
    return redirect(owner_login)


def owner_dashboard(request):
    return render(request, 'owner_dashboard.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .models import Product, ProductImage
from .forms import ProductForm, ProductImageForm

@csrf_protect
def add_products(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        images = request.FILES.getlist('images')  # Get multiple images

        if form.is_valid():
            product = form.save()  # Save product first

            # Save each image
            for img in images:
                ProductImage.objects.create(product=product, image=img)

            messages.success(request, 'Product added successfully with images!')
            return redirect('all_products')
        else:
            messages.error(request, 'Error adding product. Please check the form.')

    else:
        form = ProductForm()
    
    return render(request, 'add_products.html', {'form': form})


def all_products(request):
    products = Product.objects.all()
    return render(request, 'all_products.html', {'products': products})

def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    form = ProductForm(instance=product)
    images = ProductImage.objects.filter(product=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        new_images = request.FILES.getlist('images')
        if form.is_valid():
            product = form.save()
            for img in new_images:
                ProductImage.objects.create(product=product, image=img)
            messages.success(request, 'Product updated successfully')
            return redirect('all_products')
        else:
            messages.error(request, 'Error updating product. Please check the form')
    context = {
        'form': form,
        'images': images,
    }
    return render(request, 'update_product.html', context)

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    messages.success(request, 'Product deleted successfully')
    return redirect('all_products')