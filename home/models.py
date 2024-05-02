from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from django.conf import settings
from django.db.models import Avg
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='products')
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = CloudinaryField('image')
    on_sale = models.BooleanField(default=False)
    stock = models.IntegerField(default=50)

    def average_rating(self):
        return self.reviews.aggregate(Avg('rating'))['rating__avg'] or 0

    def rounded_average_rating(self):
        return round(self.average_rating(), 2)

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews',
                                on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    rating = models.IntegerField(default=5)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review {self.id} on {self.product}'


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} received at {self.received_at.strftime('%Y-%m-%d %H:%M')}"

