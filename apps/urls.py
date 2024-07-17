from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from apps import views
from apps.views import (ProductListView, CustomLoginView, RegisterView, ProductDetailView, ProductAdminListView,
                        CategoryListView, ProfileUpdateView)

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register_page'),
    path('product/admin', ProductAdminListView.as_view(), name='admin_list'),
    # path('product/admin/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('profile', ProfileUpdateView.as_view(), name='profile_page'),
    path('categories', CategoryListView.as_view(), name='category'),
    path('login/', views.login_page, name='login_page'),
]
