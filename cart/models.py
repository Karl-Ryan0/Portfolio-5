from django.db import models
from django.conf import settings
from home.models import Product


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return sum(item.total_price() for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items',
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def total_price(self):
        return self.quantity * self.product.price
