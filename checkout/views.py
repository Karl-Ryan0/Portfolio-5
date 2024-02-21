import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order, OrderItem
from cart.models import Cart
from .forms import ShippingAddressForm
from django.http import HttpResponseRedirect

# Create your views here.


def get_user_cart(request):
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user, defaults={'active': True})
    else:
        cart_id = request.session.get('cart_id')
        if cart_id:
            cart, _ = Cart.objects.get_or_create(id=cart_id, defaults={'active': True})
        else:
            cart = Cart.objects.create(active=True)
            request.session['cart_id'] = cart.id
    return cart


def checkout(request):
    cart = get_user_cart(request)
    if cart.items.count() == 0:
        return render(request, 'checkout/cart_empty.html')
    
    if request.method == 'POST':
        shipping_address_form = ShippingAddressForm(request.POST)
        if shipping_address_form.is_valid():
            request.session['shipping_address'] = shipping_address_form.cleaned_data
            return redirect('checkout')
    else:
        shipping_address_form = ShippingAddressForm()
    
    return render(request, 'checkout/checkout.html', {
        'cart': cart,
        'shipping_address_form': shipping_address_form
    })