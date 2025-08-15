from django import forms
from flightapp.models import Location, Ticket, Notice


# ---------- LOCATION FORM ----------
class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['initial', 'name']


# ---------- TICKET FORM ----------
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'flight_no', 'airline_name',
            'departure', 'destination',
            'departure_time', 'arrival_time',
            'original_price', 'discounted_price',
            'total_seats', 'available_seats'
        ]
        widgets = {
            'departure_time': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
            'arrival_time': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ensure correct date-time format for both fields
        self.fields['departure_time'].input_formats = ['%Y-%m-%dT%H:%M']
        self.fields['arrival_time'].input_formats = ['%Y-%m-%dT%H:%M']


# ---------- NOTICE FORM ----------
class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'message']
