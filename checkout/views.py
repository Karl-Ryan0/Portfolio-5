import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order, OrderItem
from cart.models import Cart, CartItem
from .forms import ShippingAddressForm
from django.http import HttpResponseRedirect
from .forms import ShippingAddressForm

# Create your views here.


def checkout(request):
    cart_id = request.session.get('cart_id', None)
    cart = get_object_or_404(Cart, id=cart_id) if cart_id else None

    if not cart or cart.items.count() == 0:
        # Redirect to some page indicating the cart is empty or display a message
        return render(request, 'checkout/cart_empty.html')

    shipping_address_form = ShippingAddressForm(request.POST or None)
    
    if request.method == 'POST' and shipping_address_form.is_valid():
        # Process the form and create the order here
        # For demonstration, let's assume order creation is handled inside this conditional
        # After creating the order, clear the cart and redirect to a confirmation page

        # Placeholder for order creation logic

        # Clear the cart session
        if 'cart_id' in request.session:
            del request.session['cart_id']

        # Redirect to a confirmation page
        return redirect('order_confirmation')  # Ensure you have this URL name defined in your urls.py

    # Pass both the cart and the form to the template
    return render(request, 'checkout/checkout.html', {
        'cart': cart,
        'shipping_address_form': shipping_address_form,
    })


def payment(request):
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.get(id=cart_id) if cart_id else None
    
    if request.method == 'POST' and cart:
        # Simulate payment success
        Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            total_price=cart.total_price
        )
        # Clear the cart
        CartItem.objects.filter(cart=cart).delete()
        cart.delete()
        del request.session['cart_id']
        
        return redirect('payment_success')  # Redirect to a payment success page
    
    return render(request, 'checkout/payment.html', {'cart': cart})