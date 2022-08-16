from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """Configurating for Order Line Items on admin page"""
    model = OrderLineItem

    readonly_fields = ('lineitem_total',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Configuration for Orders on admin page.
    """
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = (
        'order_number', 'date', 'delivery_cost',
        'order_total', 'grand_total')

    fields = (
        'order_number', 'date', 'first_name', 'last_name', 'email_address',
        'phone_number', 'street_address_1', 'street_address_2', 'postcode',
        'city', 'country', 'delivery_cost', 'order_total', 'grand_total')

    list_display = (
        'order_number', 'date', 'first_name', 'last_name', 'email_address',
        'delivery_cost', 'order_total', 'grand_total')

    search_fields = (
        'order_number', 'date', 'first_name', 'last_name', 'email_address',
        'street_address_1', 'street_address_2', 'postcode', 'city', 'country',
        'delivery_cost', 'order_total', 'grand_total')

    ordering = ('-date',)
