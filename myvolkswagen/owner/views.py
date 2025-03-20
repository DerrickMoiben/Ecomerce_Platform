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
from .forms import ProductForm
from .models import Product, ProductImage

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .models import Product, ProductImage
from .forms import ProductForm, ProductImageForm, ProductCreateForm


def add_products(request):
    if request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            # Create the product
            product = Product.objects.create(
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                description=form.cleaned_data['description'],
                availability=form.cleaned_data['availability']
            )

            # Handle the images
            images = request.FILES.getlist('images')
            for image in images:
                ProductImage.objects.create(product=product, image=image)

            return redirect('product_list')  # Replace 'product_list' with your product list view name
    else:
        form = ProductCreateForm()
    return render(request, 'add_product.html', {'form': form})


from django.shortcuts import render
from .models import Product

def all_products(request):
    products = Product.objects.all()
    return render(request, 'all_products.html', {'products': products})

def view_product(request):
    products = Product.objects.all()
    return render(request, 'view_products.html', {'products': products})
