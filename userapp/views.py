from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UserCreationForm, UserLoginForm, UserUpdateForm
from .models import CustomUser
from flightapp.models import Booking
from django.http import HttpResponseForbidden
from .decorators import role_required


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'userapp/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            from django.contrib.auth import authenticate, login
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid credentials")
    else:
        form = UserLoginForm()
    return render(request, 'userapp/login.html', {'form': form})


def is_admin(user):
    return user.is_authenticated and (user.is_staff or user.groups.filter(name='Admin').exists())


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def profile_view(request):
    user = request.user
    bookings = Booking.objects.filter(user=user).order_by('-booking_date')

    return render(request, 'userapp/profile.html', {
        'user': user,
        'bookings': bookings,
    })


@login_required
def edit_profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'userapp/edit_profile.html', {'form': form})


@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    # Admin-only dashboard logic (add any admin stats here)
    return render(request, 'adminapp/dashboard.html')


@role_required('admin')
def admin_only_view(request):
    # Example admin-only view
    context = {
        "message": "Welcome to the Admin-Only Page",
        "user": request.user
    }
    return render(request, 'adminapp/admin_only.html', context)
