from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LoginForm, SignupForm, EditProfileForm
from .models import Profile

from shop.models import Cart


def user_login(request):
    FALLBACK_REDIRECT = reverse('shop:home')

    if request.user.is_authenticated:
        return redirect(FALLBACK_REDIRECT)
    if request.method == 'POST':
        if (form := LoginForm(request.POST)).is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if user := authenticate(request, username=username, password=password):
                login(request, user)
                return redirect(request.GET.get('next', FALLBACK_REDIRECT))
            else:
                form.add_error(None, 'Incorrect username or password.')
    else:
        form = LoginForm()
    return render(
        request,
        'accounts/login.html',
        dict(form=form),
    )


def user_logout(request):
    logout(request)
    return redirect('shop:home')


def user_signup(request):
    if request.method == 'POST':
        if (form := SignupForm(request.POST)).is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            Cart.objects.create(user=user)
            login(request, user)
            return redirect('shop:home')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', dict(form=form))


def my_profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'accounts/my_profile.html', {'profile': profile})


def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        if (form := EditProfileForm(request.POST, request.FILES, instance=profile)).is_valid():
            p = form.save()
            return redirect('shop:home')
    else:
        form = EditProfileForm(instance=profile)
    return render(request, 'shared/form.html', {'form': form})
