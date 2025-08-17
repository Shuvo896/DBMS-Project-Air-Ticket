from datetime import datetime, timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.timezone import now
from xhtml2pdf import pisa

from .forms import FlightSearchForm, SeatSelectionForm, PaymentForm
from .models import Location, Ticket, Booking, Notice


def home_view(request):
    form = FlightSearchForm(request.POST or None)
    search_results = None
    notices = Notice.objects.all().order_by('-created_at')[:5]

    frequent_flights = []
    last_flight = None

    if request.user.is_authenticated:
        # Find most common (departure, destination) pairs
        frequent_pairs = (
            Booking.objects.filter(user=request.user, confirmed=True)
            .values('ticket__departure', 'ticket__destination')
            .annotate(pair_count=Count('id'))
            .order_by('-pair_count')
        )
        for pair in frequent_pairs[:3]:
            ticket = Ticket.objects.filter(
                departure_id=pair['ticket__departure'],
                destination_id=pair['ticket__destination']
            ).first()
            if ticket:
                frequent_flights.append(ticket)

        # Last traveled flight
        last_booking = Booking.objects.filter(
            user=request.user, confirmed=True
        ).order_by('-booking_date').first()
        if last_booking:
            last_flight = last_booking.ticket

    if request.method == 'POST' and form.is_valid():
        departure = form.cleaned_data['departure']
        destination = form.cleaned_data['destination']
        date = form.cleaned_data['date']

        print(f"Search input - Departure: {departure}, Destination: {destination}, Date (type {type(date)}): {date}")

        ticket_query = Ticket.objects.filter(
            departure=departure,
            destination=destination,
            available_seats__gt=0
        )

        if date:
            print("Sample departure times before filtering:")
            for t in ticket_query[:5]:
                print(t.departure_time, t.departure_time.date())

            start_datetime = datetime.combine(date, datetime.min.time())
            end_datetime = start_datetime + timedelta(days=1)

            ticket_query = ticket_query.filter(
                departure_time__gte=start_datetime,
                departure_time__lt=end_datetime
            )

        search_results = ticket_query.order_by('departure_time')
        print(f"Search results count: {search_results.count()}")

    context = {
        'form': form,
        'search_results': search_results,
        'notices': notices,
        'frequent_flights': frequent_flights,
        'last_flight': last_flight,
    }
    return render(request, 'home.html', context)


@login_required
def download_booking_pdf(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    html_string = render_to_string('flightapp/booking_ticket_pdf.html', {'booking': booking, 'now': now()})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="ticket_{booking.id}.pdf"'

    pisa_status = pisa.CreatePDF(html_string, dest=response)
    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=500)
    return response

@login_required
def seat_selection_view(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == "POST":
        form = SeatSelectionForm(request.POST)
        if form.is_valid():
            seats = form.cleaned_data['seats']
            if seats > ticket.available_seats:
                form.add_error('seats', 'Not enough seats available')
            else:
                booking = Booking.objects.create(
                    user=request.user,
                    ticket=ticket,
                    seats_booked=seats
                )
                return redirect('payment', booking_id=booking.id)
    else:
        form = SeatSelectionForm()
    return render(request, 'flightapp/seat_selection.html', {'form': form, 'ticket': ticket})


@login_required
def payment_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Payment processing logic placeholder
            booking.confirmed = True
            booking.ticket.available_seats -= booking.seats_booked
            booking.ticket.save()
            booking.save()
            return redirect('booking_confirmed', booking_id=booking.id)
    else:
        form = PaymentForm()
    return render(request, 'flightapp/payment.html', {'form': form, 'booking': booking})


@login_required
def booking_confirmed_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'flightapp/booking_confirmed.html', {'booking': booking})


@login_required
def cancel_booking_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == "POST" and booking.confirmed:
        booking.confirmed = False
        booking.save()
        # Optionally restore ticket's available seats
        booking.ticket.available_seats += booking.seats_booked
        booking.ticket.save()
        messages.success(request, "Your booking has been cancelled.")
    return redirect('profile')
