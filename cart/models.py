from django.db import models
from django.conf import settings
from home.models import Product


class Cart(models.Model):
    """
    Model representing a shopping cart.

    Attributes:
        user (ForeignKey): A reference to the user who owns the cart.
        Can be null for anonymous users.
        created_at (DateTimeField): The date and time when the cart was
        created, automatically set to now when the cart is created.
        active (BooleanField): A flag indicating whether the cart is active
        or has been checked out.

    Methods:
        total_price: Returns the total price of all items in the cart.
        item_count: Returns the number of items in the cart.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    @property
    def total_price(self):
        return sum(item.total_price() for item in self.items.all())

    @property
    def item_count(self):
        return self.items.count()


class CartItem(models.Model):
    """
    Model representing an item within a shopping cart.

    Attributes:
        cart (ForeignKey): A reference to the Cart that the item belongs to.
        product (ForeignKey): A reference to the Product that the item
        represents.
        quantity (IntegerField): The quantity of the product in the cart.

    Methods:
        total_price: Returns the total price for this item
        (quantity * product price).
    """
    cart = models.ForeignKey(Cart, related_name='items',
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def total_price(self):
        return self.quantity * self.product.price
