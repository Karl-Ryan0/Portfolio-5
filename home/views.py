from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, ContactMessage
from .forms import ContactForm, ProductForm, ReviewForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    """
    Renders the homepage with a selection of products and categories.
    Fetches the latest 8 products to display on the homepage.
    """
    products = Product.objects.all().order_by('-created_at')[:8]
    categories = Category.objects.all()
    return render(request, 'home/index.html', {
        'products': products,
        'categories': categories
    })


def sale_items(request):
    """
    Displays a paginated list of products that are on sale.
    Products on sale are filtered and paginated with 8 items per page.
    """
    sale_items_list = Product.objects.filter(on_sale=True)
    paginator = Paginator(sale_items_list, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home/sale_items.html', {'page_obj': page_obj})


def category_items(request, category_slug):
    """
    Displays products belonging to a specific category.
    Finds the category by its slug and then filters products by this category.
    """
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'home/category_items.html', {
        'category': category,
        'products': products
    })


def categories_processor(request):
    """
    Context processor to make all categories available across all templates.
    """
    categories = Category.objects.all()
    return {'categories': categories}


def all_products(request):
    """
    Displays a paginated list of all products.
    All products are paginated with 8 items per page.
    """
    products_list = Product.objects.all()
    paginator = Paginator(products_list, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home/all_products.html', {'page_obj': page_obj})


def contact(request):
    """
    Renders the contact form page and handles form submission.
    Upon POST request, validates the form and creates a ContactMessage object.
    """
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
    """
    Renders a success message after a contact message has been successfully
    submitted.
    """
    return render(request, 'home/contact_success.html')


def about(request):
    """
    Renders the 'About Us' page.
    """
    return render(request, 'home/about.html')


def product_detail(request, product_id):
    """
    Displays the detail page for a single product.
    Allows users to submit reviews if they are authenticated.
    """
    product = get_object_or_404(Product, pk=product_id)
    reviews = product.reviews.all()
    new_review = None

    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.product = product
            new_review.user = request.user
            new_review.save()
            return redirect('product_detail', product_id=product.id)
    else:
        review_form = ReviewForm()

    return render(request, 'home/product_detail.html', {'product': product,
                                                        'reviews': reviews,
                                                        'new_review':
                                                        new_review,
                                                        'review_form':
                                                        review_form})


def my_account(request):
    """
    Renders the user account page for logged-in users.
    """
    return render(request, 'home/my_account.html', {'user': request.user})


def staff_check(user):
    """
    Utility function to check if a user is a staff member.
    """
    return user.is_staff


@login_required
@user_passes_test(staff_check)
def edit_product(request, product_id):
    """
    Renders the edit form for a specific product and handles form submission.
    Available only to staff members.
    """
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
    """
    Handles adding a specified quantity of a product to the shopping cart.
    """
    data = json.loads(request.body)
    product_id = data.get('product_id')
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.add(product, quantity=1)

    return JsonResponse({'success': True})


def search_results(request):
    """
    Renders search results based on a query and allows sorting and filtering.
    Supports sorting by name, price, and date, and filtering by stock status
    and sale status.
    """
    query = request.GET.get('query')
    sort = request.GET.get('sort', 'name')
    in_stock = request.GET.get('in_stock', None) is not None
    on_sale = request.GET.get('on_sale', None) is not None

    results = Product.objects.all()

    if query:
        results = results.filter(name__icontains=query)

    if in_stock:
        results = results.exclude(stock=0)

    if on_sale:
        results = results.filter(on_sale=True)

    if sort == 'price_low_to_high':
        results = results.order_by('price')
    elif sort == 'price_high_to_low':
        results = results.order_by('-price')
    elif sort == 'date_newest':
        results = results.order_by('-created_at')
    elif sort == 'date_oldest':
        results = results.order_by('created_at')

    paginator = Paginator(results, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home/search_results.html', {
        'page_obj': page_obj,
        'query': query,
        'sort': sort,
        'in_stock': in_stock,
        'on_sale': on_sale
    })


@login_required
@user_passes_test(staff_check)
def add_product(request):
    """
    Renders a form to add a new product to the database and handles
    form submission.
    Available only to staff members.
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'home/add_product.html', {'form': form})
