from django.contrib import messages
from django.shortcuts import render, redirect


def landingpage(request):
    return render(request, 'landingpage.html')