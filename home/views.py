from django.shortcuts import render
from .models import Product

# Create your views here.


def index(request):
    products = Product.objects.all().order_by('-created_at')[:5]
    return render(request, 'home/index.html', {'products': products})


def sale_items(request):
    sale_items = Product.objects.filter(on_sale=True)
    return render(request, 'home/sale_items.html', {'sale_items': sale_items})
