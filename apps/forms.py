from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.forms import ModelForm

from apps.models import Product, Profile


class RegisterModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password']

    def clean_password(self):
        return make_password(self.cleaned_data.get('password'))


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class LoginForm(AuthenticationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))