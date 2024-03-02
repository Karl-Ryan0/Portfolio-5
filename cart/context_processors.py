from django.shortcuts import get_object_or_404
from home.models import Product


def cart_processor(request):
    """
    Context processor for cart data.

    This function aggregates data about the items currently in
    the user's shopping cart,
    including the total number of items, their cumulative cost,
    and a list of the items
    themselves with detailed information.

    Args:
        request: The HTTP request object.

    Returns:
        A dictionary context containing cart items,
        their total count, total price,
        and the grand total price of all items.
        This context can be used to populate
        cart data across the site.
    """
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
