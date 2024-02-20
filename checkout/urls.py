from django.urls import path
from .views import checkout
from .views import cart_empty

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('cart/empty/', cart_empty, name='cart_empty'),
]