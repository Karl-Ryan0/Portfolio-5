from django.urls import path
from .views import add_to_cart, cart_detail, update_cart_item, remove_item

urlpatterns = [
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_detail, name='cart_detail'),
    path('update_cart_item/<int:item_id>/',
         update_cart_item, name='update_cart_item'),
    path('cart/remove_item/<int:item_id>/', remove_item, name='remove_item'),
]
