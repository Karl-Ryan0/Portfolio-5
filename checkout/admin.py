from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.

admin.site.register(OrderItem)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'paid_amount', 'created_at']
    list_filter = ['created_at', 'user']
    date_hierarchy = 'created_at'
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
