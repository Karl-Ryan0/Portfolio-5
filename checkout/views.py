import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order, OrderItem
from cart.models import Cart, CartItem
from .forms import ShippingAddressForm
from django.http import HttpResponseRedirect
from .forms import ShippingAddressForm
from home.views import Product

# Create your views here.


def checkout(request):
    cart_session_data = request.session.get('cart', {})
    cart_products = []
    total_price = 0

    for item_id, quantity in cart_session_data.items():
        product = get_object_or_404(Product, pk=item_id)
        total_item_price = product.price * quantity
        total_price += total_item_price
        cart_products.append({
            'product_id': item_id,
            'quantity': quantity,
            'product': product,
            'total_item_price': total_item_price,
        })

    if not cart_products:
        messages.error(request, "Your cart is empty.")
        return redirect('cart_detail')

    shipping_address_form = ShippingAddressForm(request.POST or None)

    if request.method == 'POST' and shipping_address_form.is_valid():
        # Proceed with order creation and form handling
        # ...
        # Make sure to pass the necessary order_id or similar parameter
        return redirect('order_confirmation')

    return render(request, 'checkout/checkout.html', {
        'cart_products': cart_products,
        'total_price': total_price,
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

        # Redirect to a payment success page
        return redirect('payment_success')

    return render(request, 'checkout/payment.html', {'cart': cart})
