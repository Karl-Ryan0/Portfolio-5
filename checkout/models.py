from django.db import models
from django.conf import settings
from home.models import Product
from cart.models import Cart
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='orders')
    cart = models.OneToOneField(
        Cart, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_id = models.CharField(max_length=120, blank=True)


@receiver(post_save, sender=Order)
def set_order_id(sender, instance, created, **kwargs):
    if created:
        instance.order_id = f"ORDER-{instance.pk}"
        instance.save()


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def get_cost(self):
        return self.price * self.quantity


class ShippingAddress(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, related_name='shipping_address')
    full_name = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.full_name}, {self.address_line_1}, {self.city}, {self.postal_code}, {self.country}"
