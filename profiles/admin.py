from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Configuration for user profiles on admin page.
    """
    fields = (
        'user', 'phone_number', 'street_address_1',
        'street_address_2', 'postcode', 'city',
        'country')

    list_display = ('user',)

    search_fields = (
        'user__username', 'phone_number', 'street_address_1',
        'street_address_2', 'postcode', 'city',
        'country')
