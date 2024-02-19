from .models import Cart


def cart_processor(request):
    cart_id = request.session.get('cart_id', None)
    cart = None
    total_price = 0
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        total_price = cart.total_price
    elif cart_id:
        try:
            cart = Cart.objects.get(id=cart_id)
            total_price = cart.total_price
        except Cart.DoesNotExist:
            pass

    return {
        'cart': cart,
        'total_price': total_price,
        'cart_item_count': cart.item_count if cart else 0
    }
