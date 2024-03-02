import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order, OrderItem
from .forms import ShippingAddressForm
from home.views import Product

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    """
    Display the checkout page with cart items and a form for shipping address.

    Retrieves items from the cart stored in the session, calculates the total
    price and displays the shipping address form. Upon form submission, if
    valid, stores the shipping address in the session and redirects to the
    payment page. Redirects to the cart detail page with an error message if
    the cart is empty.
    """
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
        request.session[
            'shipping_address'] = shipping_address_form.cleaned_data
        return redirect('payment')

    return render(request, 'checkout/checkout.html', {
        'cart_products': cart_products,
        'total_price': total_price,
        'shipping_address_form': shipping_address_form,
    })


def payment(request):
    """
    Process payment using Stripe and create an order.

    Attempts to create a Stripe charge with the total price of cart items. Upon
    successful charge, creates an Order with associated OrderItems and shipping
    address, clears the cart from the session, and redirects to the order
    confirmation page. Displays an error and redirects to the payment page
    upon failure.
    """
    cart_session_data = request.session.get('cart', {})

    if not cart_session_data:
        messages.error(request, "Your cart is empty.")
        return redirect('cart_detail')

    total_price = 0
    for item_id, quantity in cart_session_data.items():
        product = get_object_or_404(Product, pk=item_id)
        total_price += product.price * quantity

    if request.method == 'POST':
        stripe_token = request.POST.get('stripeToken')
        try:
            charge = stripe.Charge.create(
                amount=int(total_price * 100),
                currency="eur",
                source=stripe_token,
                description="Charge for a purchase"
            )

            if charge['paid']:
                shipping_address_data = request.session.get(
                    'shipping_address', {})
                order = Order.objects.create(
                    user=request.user if request.user.is_authenticated else None,
                    total_price=total_price,
                    email=shipping_address_data.get('email'),
                    address=shipping_address_data.get(
                        'address_line_1') + " " + shipping_address_data.get('address_line_2', ''),
                    postal_code=shipping_address_data.get('postal_code'),
                    city=shipping_address_data.get('city'),
                    country=shipping_address_data.get('country')
                )

                for item_id, quantity in cart_session_data.items():
                    product = get_object_or_404(Product, pk=item_id)
                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        quantity=quantity,
                        price=product.price
                    )

                del request.session['cart']
                messages.success(request, "Your payment was successful.")

                return redirect('order_confirmation', order_id=order.id)

        except stripe.error.StripeError as e:
            messages.error(request, "There was an error with your payment.")

    return render(request, 'checkout/payment.html', {
        'total_price': total_price,
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
    })


def order_confirmation(request, order_id):
    """
    Display an order confirmation page to the user.

    Retrieves an Order by its ID and renders the order confirmation page with
    order details.
    """
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'checkout/order_confirmation.html', {'order':
                                                                order})
