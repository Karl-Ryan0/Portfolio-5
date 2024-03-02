from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm, UserProfileForm
from .models import UserProfile
from checkout.models import Order
from home.models import ContactMessage
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.


@login_required
def profile(request):
    """
    Display the user's profile page with their order history and profile
    details.
    """
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST' and 'change_password' in request.POST:
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
    else:
        password_form = PasswordChangeForm(request.user)
    context = {'user_profile': user_profile,
               'password_form': password_form, 'orders': orders}
    return render(request, 'my_account/profile.html', context)


@login_required
def edit_profile(request):
    """
    Allows the user to edit their profile information including mailing list
    subscriptions.
    """
    user_profile, created = UserProfile.objects.get_or_create(
        user=request.user)

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=user_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)

    return render(request, 'my_account/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required
def view_messages(request):
    """
    Allows staff users to view contact messages received from users.
    This view is restricted to staff members and paginates the messages for
    easier navigation.
    """
    if not request.user.is_staff:
        return redirect('home')

    messages_list = ContactMessage.objects.all().order_by('-received_at')
    paginator = Paginator(messages_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'my_account/messages.html', {'page_obj': page_obj})


@login_required
def delete_message(request, message_id):
    """
    Allows staff users to delete a specific message by ID.
    """
    if request.user.is_staff:
        message = get_object_or_404(ContactMessage, id=message_id)
        message.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def order_detail(request, order_id):
    """
    Displays the details of a specific order, accessible only by the orderer.
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'my_account/order_detail.html', {'order': order})
