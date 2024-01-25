from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product

# Register your models here.

admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'description', 'product_image')

    def product_image(self, obj):
        return format_html('<img src="{}" width="auto" height="100px"/>',
                           obj.image.url)

    product_image.short_description = 'Image'
    product_image.allow_tags = True
