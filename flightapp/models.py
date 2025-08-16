from django.db import models
from userapp.models import CustomUser


class Location(models.Model):
    initial = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.initial})"

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"
        ordering = ['name']


class Ticket(models.Model):
    departure = models.ForeignKey('Location', related_name='departures', on_delete=models.CASCADE)
    destination = models.ForeignKey('Location', related_name='destinations', on_delete=models.CASCADE)
    flight_no = models.CharField(max_length=20, unique=True)
    airline_name = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_seats = models.IntegerField()
    available_seats = models.IntegerField()

    @property
    def travel_time(self):
        """Returns the duration of the flight as a timedelta."""
        return self.arrival_time - self.departure_time

    def __str__(self):
        return f"{self.flight_no} | {self.airline_name} | {self.departure} → {self.destination} on {self.departure_time.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
        ordering = ['departure_time']


class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    seats_booked = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.email} booked {self.seats_booked} seat(s) on {self.ticket.flight_no}"

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ['-booking_date']


class Notice(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Notice"
        verbose_name_plural = "Notices"
        ordering = ['-created_at']
