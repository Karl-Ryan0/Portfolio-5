from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, ContactMessage
from .forms import ContactForm, ProductForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_POST

# Create your views here.


def index(request):
    products = Product.objects.all().order_by('-created_at')[:4]
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


def my_account(request):
    return render(request, 'home/my_account.html', {'user': request.user})


def staff_check(user):
    return user.is_staff


@login_required
@user_passes_test(staff_check)
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'home/edit_product.html', {'form': form, 'product': product})


def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data.get('product_id')
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.add(product, quantity=1)

    return JsonResponse({'success': True})


def search_results(request):
    query = request.GET.get('query')
    if query:
        results = Product.objects.filter(name__icontains=query)
    else:
        results = Product.objects.none()
    
    return render(request, 'home/search_results.html', {'results': results})
