from django.urls import path
from .views import checkout,  payment, order_confirmation


urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('payment/', payment, name='payment'),
    path('order_confirmation/<int:order_id>/',
         order_confirmation, name='order_confirmation'),
]
