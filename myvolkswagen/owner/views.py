from django.shortcuts import render, redirect
from .forms import OwnerCreationForm, OwnerLoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login   
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect

def homepage(requst):
    return render(requst, 'homepage.html')

@csrf_protect
def owner_singup(requst):
    if requst.method == 'POST':
        form = OwnerCreationForm(requst.POST)
        if form.is_valid():
            form.save()
            return redirect('owner_login')
        
    else:
        form = OwnerCreationForm()
    return render(requst, 'owner_singup.html', {'form': form})

def owner_login(requst):
    return render(requst, 'owner_login.html')

def owner_logout(requst):
    return render(requst, 'owner_logout.html')
