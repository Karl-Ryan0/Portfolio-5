from django.shortcuts import render, redirect
from .models import Order, OrderItem
from cart.models import Cart
from .forms import ShippingAddressForm

# Create your views here.


def checkout(request):
    cart_id = request.session.get('cart_id')
    cart = None

    if cart_id:
        cart = Cart.objects.filter(id=cart_id).first()
    elif request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user, active=True).first()

    if not cart or cart.items.count() == 0:
        return render(request, 'checkout/cart_empty.html', {})

    shipping_address_form = ShippingAddressForm()

    if request.method == 'POST':
        shipping_address_form = ShippingAddressForm(request.POST)
        if shipping_address_form.is_valid():
            shipping_address = shipping_address_form.save(commit=False)
            if request.user.is_authenticated:
                shipping_address.user = request.user
            shipping_address.save()

            order = Order.objects.create(
                user=request.user if request.user.is_authenticated else None,
                paid_amount=cart.total_price,
                shipping_address=shipping_address
            )

            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    price=item.product.price,
                    quantity=item.quantity
                )

            cart.active = False
            cart.save()

            if not request.user.is_authenticated:
                del request.session['cart_id']

            return redirect('checkout:order_confirmation', order_id=order.id)

    else:
        shipping_address_form = ShippingAddressForm()

    return render(request, 'checkout/checkout.html', {
        'cart': cart,
        'shipping_address_form': ShippingAddressForm()
    })

