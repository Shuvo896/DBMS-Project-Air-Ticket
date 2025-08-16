from django import forms
from .models import Location, Ticket

class FlightSearchForm(forms.Form):
    departure = forms.ModelChoiceField(queryset=Location.objects.all())
    destination = forms.ModelChoiceField(queryset=Location.objects.all())
    date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

class SeatSelectionForm(forms.Form):
    seats = forms.IntegerField(min_value=1, max_value=4, label="Number of Seats")

class PaymentForm(forms.Form):
    PAYMENT_METHODS = [
        ('card', 'Card'),
        ('bkash', 'Bkash'),
        ('nagad', 'Nagad'),
        ('rocket', 'Rocket'),
        ('bank', 'Bank Transfer')
    ]
    method = forms.ChoiceField(choices=PAYMENT_METHODS)

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        widgets = {
            'departure_time': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},  # HTML5 date+time picker
                format='%Y-%m-%dT%H:%M'
            ),
            'arrival_time': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set correct display/input format for existing values
        for field in ['departure_time', 'arrival_time']:
            self.fields[field].input_formats = ['%Y-%m-%dT%H:%M']
