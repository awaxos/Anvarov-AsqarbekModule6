import re

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, DetailView

from apps.forms import RegisterModelForm, ProductForm, LoginForm
from apps.models import Category, Product, Profile



class CustomLoginView(TemplateView):
    template_name = 'apps/auth/login.html'

    def post(self, request, *args, **kwargs):
        email = re.sub(r'\D', '', request.POST.get('email'))
        user = User.objects.filter(email=email).first()
        if not user:
            user = User.objects.create_user(email=email, password=request.POST['password'])
            login(request, user)
            return redirect('home')
        else:
            user = authenticate(request, username=user.email, password=request.POST['password'])
            if user:
                login(request, user)
                return redirect('home')

            else:
                context = {
                    "messages_error": ["Invalid password"]
                }
                return render(request, template_name='apps/auth/login.html', context=context)


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'apps/include_base/base.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data['categories'] = Category.objects.all()
        return data


class RegisterView(CreateView):
    form_class = RegisterModelForm
    template_name = 'apps/auth/register.html'
    success_url = 'login'


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'apps/product/product-detail.html'


class ProductAdminListView(ListView):
    queryset = Product.objects.all()
    template_name = 'apps/product/admin-product-list.html'
    context_object_name = 'products'


class ProfileUpdateView(View):
    def get(self, request):
        Profile.objects.filter().first().delete()
        return redirect('profile_page')


class CategoryListView(ListView):
    queryset = Product.objects.all()
    template_name = 'apps/product/category.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data['categories'] = Category.objects.all()
        return data


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # Redirect to profile or dashboard page
    else:
        form = LoginForm()

    return render(request, 'apps/auth/login.html', {'form': form})