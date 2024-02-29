from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, ContactMessage, Review

# Register your models here.

admin.site.register(Category)
admin.site.register(ContactMessage)
admin.site.register(Review)


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'description',
                    'on_sale', 'product_image')
    list_filter = ('category', 'on_sale')
    search_fields = ('name', 'description', 'category__name')
    ordering = ('name', 'price')
    readonly_fields = ('get_image_preview',)
    inlines = [ReviewInline]

    def average_rating(self, obj):
        return obj.rounded_average_rating()
    average_rating.short_description = 'Avg Rating'

    def product_image(self, obj):
        return format_html('<img src="{}" width="auto" height="100px"/>',
                           obj.image.url)

    product_image.short_description = 'Image'
    product_image.allow_tags = True

    def get_image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:150px; width:auto;" />', obj.image.url)
        return "(No image)"

    get_image_preview.short_description = 'Image Preview'
