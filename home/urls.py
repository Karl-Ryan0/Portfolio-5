from django.contrib import admin
from django.urls import path
from . import views
from .views import sale_items, category_items, all_products, contact, contact_success, product_detail


urlpatterns = [
    path('', views.index, name='home'),
    path('sale/', sale_items, name='sale_items'),
    path('category/<slug:category_slug>/',
         category_items, name='category_items'),
    path('products', all_products, name='all_products'),
    path('contact/', contact, name='contact'),
    path('contact_success/', contact_success, name='contact_success'),
    path('about', views.about, name='about'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
]
