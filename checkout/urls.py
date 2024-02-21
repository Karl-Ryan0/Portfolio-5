from django.urls import path
from .views import checkout

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    # path('payment/<int:order_id>/', payment, name='payment'),
    # path('order_confirmation/<int:order_id>/',
    #      order_confirmation, name='order_confirmation'),
]
