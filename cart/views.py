from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem, Product
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(
        product=product, cart=cart)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_detail')


@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/cart_detail.html', {'cart': cart})


@login_required
def update_cart_item(request, item_id):
    if request.method == 'POST':
        quantity = request.POST.get('quantity', 1)
        try:
            cart_item = CartItem.objects.get(
                id=item_id, cart__user=request.user)
            cart_item.quantity = int(quantity)
            cart_item.save()
        except CartItem.DoesNotExist:
            pass  # Handle error or do nothing
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
