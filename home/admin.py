from django.contrib import admin
from .models import Inquiry


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    """Configuration for Inquiry table on admin page"""
    list_filter = ('created_on',)
    list_display = ('first_name', 'last_name', 'email_address', 'created_on')
    search_fields = ('first_name', 'last_name', 'email_address')
