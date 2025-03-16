from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Products, ProductsImages
from django.forms import inlineformset_factory

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
        fields = ['name', 'price', 'description', 'availablity']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Enter product name'}),
            'price': forms.NumberInput(attrs={'placeholder':'Enter product price'}),
            'description': forms.Textarea(attrs={'placeholder':'Enter product description'}),
        }


class ProductsImagesForm(forms.ModelForm):
    class Meta:
        model = ProductsImages
        fields = ['image']


#to handle formset for images upto 10 images
productImagesFormset = inlineformset_factory(
    Products,
    ProductsImages,
    form=ProductsImagesForm,
    extra=10,
    can_delete=True #to allow deleting images
)