from django.contrib import admin
from django.urls import path
from . import views
from .views import sale_items, category_items, all_products


urlpatterns = [
    path('', views.index, name='home'),
    path('sale/', sale_items, name='sale_items'),
    path('category/<slug:category_slug>/',
         category_items, name='category_items'),
    path('products', all_products, name='all_products'),
]
