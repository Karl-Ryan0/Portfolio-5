from django.shortcuts import render, redirect
from .models import Order, OrderItem
from cart.models import Cart

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

    if request.method == 'POST':

        order = Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            paid_amount=cart.total_price()
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

    return render(request, 'checkout/checkout.html', {'cart': cart})


def cart_empty(request):
    return render(request, 'checkout/cart_empty.html')