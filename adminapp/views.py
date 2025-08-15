from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from flightapp.models import Location, Ticket, Notice, Booking
from userapp.models import CustomUser
from .forms import LocationForm, TicketForm, NoticeForm


# ✅ Unified admin access check
def is_admin(user):
    """Allow access if user is staff, superuser, or has role 'admin' or in Admin group."""
    return user.is_authenticated and (
        user.is_staff
        or user.is_superuser
        or getattr(user, 'role', None) == 'admin'
        or user.groups.filter(name='Admin').exists()
    )


# ---------- DASHBOARD ----------
@login_required(login_url='login')
@user_passes_test(is_admin, login_url='home')
def dashboard(request):
    """Admin dashboard summary stats"""
    context = {
        'total_users': CustomUser.objects.count(),
        'total_tickets': Ticket.objects.count(),
        'total_bookings': Booking.objects.count(),
        'total_notices': Notice.objects.count()
    }
    return render(request, 'adminapp/dashboard.html', context)


# ---------- LOCATION ----------
@login_required(login_url='login')
@user_passes_test(is_admin, login_url='home')
def location_list(request):
    locations = Location.objects.all()
    return render(request, 'adminapp/locations_list.html', {'locations': locations})


@login_required(login_url='login')
@user_passes_test(is_admin, login_url='home')
def location_add(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel:location_list')
    else:
        form = LocationForm()
    return render(request, 'adminapp/location_form.html', {'form': form})


@login_required(login_url='login')
@user_passes_test(is_admin, login_url='home')
def location_edit(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect('admin_panel:location_list')
    else:
        form = LocationForm(instance=location)
    return render(request, 'adminapp/location_form.html', {'form': form})


@login_required(login_url='login')
@user_passes_test(is_admin, login_url='home')
def location_delete(request, pk):
    location = get_object_or_404(Location, pk=pk)
    location.delete()
    return redirect('admin_panel:location_list')


# ---------- TICKET ----------
@login_required(login_url='login')
@user_passes_test(is_admin, login_url='home')
def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'adminapp/tickets_list.html', {'tickets': tickets})


@login_required(login_url='login')
@user_passes_test(is_admin, login_url='home')
def ticket_add(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel:ticket_list')
    else:
        form = TicketForm()
    return render(request, 'adminapp/ticket_form.html', {'form': form})


@login_required(login_url='login')
@user_passes_test(is_admin, login_url='home')
def ticket_edit(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('admin_panel:ticket_list')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'adminapp/ticket_form.html', {'form': form})


# ---------- NOTICE ----------
@login_required(login_url='login')
@user_passes_test(is_admin, login_url='home')
def notice_list(request):
    notices = Notice.objects.all()
    return render(request, 'adminapp/notices_list.html', {'notices': notices})


@login_required(login_url='login')
@user_passes_test(is_admin, login_url='home')
def notice_add(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel:notice_list')
    else:
        form = NoticeForm()
    return render(request, 'adminapp/notice_form.html', {'form': form})


# ---------- USER LIST ----------
@login_required(login_url='login')
@user_passes_test(is_admin, login_url='home')
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'adminapp/users_list.html', {'users': users})
