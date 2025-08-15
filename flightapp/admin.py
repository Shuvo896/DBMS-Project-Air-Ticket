from django.contrib import admin
from .models import Location, Ticket, Booking, Notice

admin.site.register(Location)
admin.site.register(Ticket)
admin.site.register(Booking)
admin.site.register(Notice)
