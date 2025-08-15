from django.urls import path
from . import views

urlpatterns = [
    # path('search/', views.search_flights_view, name='search_flights'),  # Removed because search is now on home page
    path('seat-selection/<int:ticket_id>/', views.seat_selection_view, name='seat_selection'),
    path('payment/<int:booking_id>/', views.payment_view, name='payment'),
    path('confirmed/<int:booking_id>/', views.booking_confirmed_view, name='booking_confirmed'),
    
]
