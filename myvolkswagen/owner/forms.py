from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Products

class OwnerCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','username', 'email', 'password1', 'password2']


class OwnerLoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'Enter your username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your password'}))



class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
