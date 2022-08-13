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
        'order_number', 'date', 'first_name', 'last_name', 'email', 'phone',
        'address1', 'address2', 'postcode', 'city', 'country',
        'delivery_cost', 'order_total', 'grand_total')

    list_display = (
        'order_number', 'date', 'first_name', 'last_name', 'email',
        'delivery_cost', 'order_total', 'grand_total')

    search_fields = (
        'order_number', 'date', 'first_name', 'last_name', 'email',
        'address1', 'address2', 'postcode', 'city', 'country',
        'delivery_cost', 'order_total', 'grand_total')

    ordering = ('-date',)
