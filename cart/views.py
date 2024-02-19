from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem, Product

# Create your views here.


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_id = request.session.get('cart_id')

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(
            user=request.user, defaults={'user': request.user})
    else:
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id

    cart_item, created = CartItem.objects.get_or_create(
        product=product, cart=cart, defaults={'product': product, 'cart': cart}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_detail')


def cart_detail(request):
    cart_id = request.session.get('cart_id')
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    elif cart_id:
        cart = Cart.objects.get(id=cart_id)
    else:
        cart = None

    return render(request, 'cart/cart_detail.html', {'cart': cart})


def update_cart_item(request, item_id):
    if request.method == 'POST':
        quantity = request.POST.get('quantity', 1)
        try:
            if request.user.is_authenticated:
                cart_item = CartItem.objects.get(
                    id=item_id, cart__user=request.user)
            else:
                cart_id = request.session.get('cart_id')
                if cart_id:
                    cart_item = CartItem.objects.get(
                        id=item_id, cart_id=cart_id)
                else:
                    return redirect('cart_error')
            cart_item.quantity = int(quantity)
            cart_item.save()
        except CartItem.DoesNotExist:
            pass
        return redirect('cart_detail')
