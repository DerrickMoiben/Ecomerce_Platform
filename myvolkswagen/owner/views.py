from django.shortcuts import render, redirect
from .forms import OwnerCreationForm, OwnerLoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login   
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages


def homepage(requst):
    return render(requst, 'homepage.html')

@csrf_protect
def owner_singup(request):
    if request.method == 'POST':
        form = OwnerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('owner_login')   
    else:
        form = OwnerCreationForm()
    return render(request, 'owner_singup.html', {'form': form})

def owner_login(request):
    if request.method == 'POST':
        form = OwnerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password =form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.sucess(request, 'You are now logged in successfully')
                return redirect('homepage')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = OwnerLoginForm()
    context = {
        'form': form,
        'messages': messages,

    }
    return render(request, 'owner_login.html', context)

def owner_logout(request):
    return render(request, 'owner_logout.html')
