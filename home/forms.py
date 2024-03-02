from django import forms
from .models import Product, Review


class ContactForm(forms.Form):
    """
    A form for website visitors to send messages to the site administrators.
    """
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class ProductForm(forms.ModelForm):
    """
    A form for creating or updating product details in the database.
    """
    class Meta:
        model = Product
        fields = ['name', 'category', 'description',
                  'price', 'image', 'on_sale']


class ReviewForm(forms.ModelForm):
    """
    A form for submitting reviews for products.
    """
    class Meta:
        model = Review
        fields = ['rating', 'comment']
