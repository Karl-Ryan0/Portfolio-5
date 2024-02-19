from .models import Cart


def cart_processor(request):
    cart_id = request.session.get('cart_id', None)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        if cart_id is None:
            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id
        else:
            cart, created = Cart.objects.get_or_create(id=cart_id)
            if created:
                request.session['cart_id'] = cart.id

    return {'cart': cart}
