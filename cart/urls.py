from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_detail, name='cart_detail'),
    path('add_to_cart/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('adjust_cart/<item_id>/', views.adjust_cart, name='adjust_cart'),
    path('remove_from_cart/<item_id>/', views.remove_from_cart, name='remove_from_cart'),
]