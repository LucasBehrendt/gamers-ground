from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Configuration for user profiles on admin page.
    """
    fields = (
        'user', 'default_phone_number', 'default_street_address_1',
        'default_street_address_2', 'default_postcode', 'default_city',
        'default_country')

    list_display = ('user',)

    search_fields = (
        'user__username', 'default_phone_number', 'default_street_address_1',
        'default_street_address_2', 'default_postcode', 'default_city',
        'default_country')
