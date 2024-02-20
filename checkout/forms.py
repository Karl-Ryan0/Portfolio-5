from django import forms
from .models import ShippingAddress


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['full_name', 'address_line_1',
                  'address_line_2', 'city', 'postal_code', 'country']
