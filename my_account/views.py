from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm
from .models import UserProfile

# Create your views here.


@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {'user_profile': user_profile}
    return render(request, 'my_account/profile.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserEditForm(instance=request.user)

    return render(request, 'my_account/edit_profile.html', {'form': form})
