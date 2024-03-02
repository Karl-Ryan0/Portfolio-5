from django import forms


class ShippingAddressForm(forms.Form):
    """
    A form for collecting shipping address information from a user.

    This form is used during the checkout process to collect the user's full
    name, email address, and shipping address details, including an optional
    second address line, city, postal code, and country.
    The `email` field is used to send order confirmation and shipping updates.
    The address fields are required to process the shipping of purchased items.
    """
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    address_line_1 = forms.CharField(max_length=100)
    address_line_2 = forms.CharField(max_length=100, required=False)
    city = forms.CharField(max_length=50)
    postal_code = forms.CharField(max_length=20)
    country = forms.CharField(max_length=50)
