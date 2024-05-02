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
        fields = ['name', 'category', 'description', 'price', 'image', 'on_sale']

    def clean_price(self):
        """
        Custom validation to ensure that price is a positive value.
        """
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError("Price must be a positive value.")
        return price


class ReviewForm(forms.ModelForm):
    """
    A form for submitting reviews for products.
    """
    class Meta:
        model = Review
        fields = ['rating', 'comment']
