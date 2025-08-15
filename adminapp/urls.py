from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # path('login/', views.login_view, name='login'),

    # Locations
    path('locations/', views.location_list, name='location_list'),
    path('locations/add/', views.location_add, name='location_add'),
    path('locations/edit/<int:pk>/', views.location_edit, name='location_edit'),
    path('locations/delete/<int:pk>/', views.location_delete, name='location_delete'),

    # Tickets
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('tickets/add/', views.ticket_add, name='ticket_add'),
    path('tickets/edit/<int:pk>/', views.ticket_edit, name='ticket_edit'),
    # Notices
    path('notices/', views.notice_list, name='notice_list'),
    path('notices/add/', views.notice_add, name='notice_add'),

    # Users
    path('users/', views.user_list, name='user_list'),
]
