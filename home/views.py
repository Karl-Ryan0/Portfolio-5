from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, ContactMessage
from .forms import ContactForm

# Create your views here.


def index(request):
    products = Product.objects.all().order_by('-created_at')[:12]
    categories = Category.objects.all()
    return render(request, 'home/index.html', {
        'products': products,
        'categories': categories
    })


def sale_items(request):
    sale_items = Product.objects.filter(on_sale=True)
    return render(request, 'home/sale_items.html', {'sale_items': sale_items})


def category_items(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'home/category_items.html', {
        'category': category,
        'products': products
    })


def categories_processor(request):
    categories = Category.objects.all()
    return {'categories': categories}


def all_products(request):
    products = Product.objects.all()
    return render(request, 'home/all_products.html', {'products': products})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'home/contact.html', {'form': form})


def contact_success(request):
    return render(request, 'home/contact_success.html')


def about(request):
    return render(request, 'home/about.html')


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'home/product_detail.html', {'product': product})
