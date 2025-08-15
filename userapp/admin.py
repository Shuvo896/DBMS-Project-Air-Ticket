from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser
from .forms import UserCreationForm
from django import forms

class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('email', 'username', 'phone_no', 'password'),
        }),
    )

    form = UserCreationForm
    list_display = ('email', 'username', 'phone_no', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username', 'phone_no')
    ordering = ('email',)
    filter_horizontal = ()
    fieldsets = (
        (None, {'fields': ('email', 'username', 'phone_no', 'password')}),
        ('Personal info', {'fields': ('gender', 'date_of_birth', 'nationality', 'address', 'postal_code', 'passport_no', 'profile_picture')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
    )

admin.site.register(CustomUser, UserAdmin)
