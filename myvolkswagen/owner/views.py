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

@csrf_protect
def add_products(request):
    if request.method == 'POST':
        prod = Product()
        prod.name = request.POST['name']
        prod.price = request.POST['price']
        prod.description = request.POST['description']
        prod.availability = request.POST['availability']

        if len (request.FILES) != 0:
            prod.image = request.FILES['image']
        prod.save()
        messages.success(request, 'Product added successfully')
        return redirect('all_products')
    return render(request, 'add_products.html')

from django.shortcuts import render
from .models import Product

def all_products(request):
    products = Product.objects.all()
    return render(request, 'all_products.html', {'products': products})

def view_product(request):
    products = Product.objects.all()
    return render(request, 'view_products.html', {'products': products})
