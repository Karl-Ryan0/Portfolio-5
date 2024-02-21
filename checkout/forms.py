from django import forms
from .models import ShippingAddress


class ShippingAddressForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    address_line_1 = forms.CharField(max_length=100)
    address_line_2 = forms.CharField(max_length=100, required=False)
    city = forms.CharField(max_length=50)
    postal_code = forms.CharField(max_length=20)
    country = forms.CharField(max_length=50)
