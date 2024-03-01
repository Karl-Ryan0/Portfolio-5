from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from home.models import Product


def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_products = []
    total_price = 0

    for item_id, quantity in cart.items():
        product = Product.objects.get(id=item_id)
        total_item_price = product.price * quantity
        total_price += total_item_price

        cart_products.append({
            'product_id': item_id,
            'quantity': quantity,
            'product': product,
            'total_item_price': total_item_price,
        })

    return render(request, 'cart/cart_detail.html', {
        'cart_products': cart_products,
        'total_price': total_price,
    })


def add_to_cart(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    """Add a quantity of the specified product to the shopping cart"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', 'cart_detail')
    cart = request.session.get('cart', {})

    if item_id in cart:
        cart[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    print(f"Cart after adding: {request.session.get('cart')}")
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
    else:
        cart.pop(item_id, None)
        messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('cart_detail'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""
    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})

        if item_id in cart:  # Check if the item exists in the cart before popping
            cart.pop(item_id)  # Safely remove the item
            messages.success(request, f'Removed {product.name} from your cart')
        else:
            messages.info(request, "The item was not in your cart.")

        request.session['cart'] = cart
        return redirect('cart_detail')  # Redirect back to the cart detail page

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return redirect('cart_detail')  # Ensure redirection even in case of error