import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order, OrderItem
from cart.models import Cart
from .forms import ShippingAddressForm
from django.http import HttpResponseRedirect

# Create your views here.


def checkout(request):
    cart_id = request.session.get('cart_id')
    cart = None

    if cart_id:
        cart = Cart.objects.get(id=cart_id)
    elif request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user, active=True).first()

    if not cart or cart.items.count() == 0:
        return render(request, 'checkout/cart_empty.html', {})

    shipping_address_form = ShippingAddressForm(request.POST or None)

    if request.method == 'POST' and shipping_address_form.is_valid():
        # Instead of saving, put the form's cleaned data into the session
        request.session['shipping_address'] = shipping_address_form.cleaned_data

        # Ensure to call the method or access the attribute correctly
        total_price_value = cart.total_price() if callable(
            cart.total_price) else cart.total_price
        total_amount_in_cents = int(total_price_value * 100)

        order = Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            paid_amount=total_price_value,
        )

        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                price=item.product.price,
                quantity=item.quantity
            )

        cart.delete()  # or cart.active = False; cart.save()

        if not request.user.is_authenticated:
            del request.session['cart_id']

        # Redirect to a different step, like payment, with order ID
        return redirect('checkout:payment', order_id=order.id)

    return render(request, 'checkout/checkout.html', {
        'cart': cart,
        'shipping_address_form': shipping_address_form,
        'total_amount_in_cents': total_amount_in_cents if 'total_amount_in_cents' in locals() else 0
    })


stripe.api_key = settings.STRIPE_SECRET_KEY


def payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":
        try:
            charge = stripe.Charge.create(
                amount=int(order.paid_amount * 100),
                currency='usd',
                description='Example charge',
                source=request.POST['stripeToken']
            )

            if charge['paid']:
                order.paid = True
                order.save()
                return redirect('order_confirmation', order_id=order.id)
        except stripe.error.StripeError as e:
            messages.error(request, "There was an error with your payment.")

    context = {
        'order': order,
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
    }
    return render(request, 'checkout/payment.html', context)


def order_confirmation(request, order_id):
    return render(request, 'checkout/order_confirmation.html', {'order_id': order_id})
