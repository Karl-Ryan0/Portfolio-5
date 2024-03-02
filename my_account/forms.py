from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile


@login_required
class UserEditForm(forms.ModelForm):
    """
    A form for editing basic information of a User model instance.
    Allows users to update their first name, last name, and email address.
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


@login_required
class UserProfileForm(forms.ModelForm):
    """
    A form for editing additional information in a UserProfile model instance.

    Allows users to opt in or out of mailing lists for shopping and blog
    updates.
    """
    class Meta:
        model = UserProfile
        fields = ['shopping_mailing_list', 'blog_mailing_list']
