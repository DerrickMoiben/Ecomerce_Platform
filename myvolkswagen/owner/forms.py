from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Product
from django.forms import inlineformset_factory

class OwnerCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','username', 'email', 'password1', 'password2']


class OwnerLoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'Enter your username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your password'}))




from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    images = forms.ImageField(
        widget=forms.FileInput(),  # Use FileInput, not ClearableFileInput
        required=False,
        help_text='Upload up to 6 images.'
    )

    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'availability']

    def clean_images(self):
        images = self.files.getlist('images')
        if len(images) > 6:
            raise forms.ValidationError("You can upload a maximum of 6 images.")
        return images