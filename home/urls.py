from django.contrib import admin
from django.urls import path
from . import views
from .views import sale_items


urlpatterns = [
    path('', views.index, name='home'),
    path('sale/', sale_items, name='sale_items',)
]
