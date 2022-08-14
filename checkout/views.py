from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from .models import Order


class Checkout(generic.CreateView):
    """Renders checkout page with payment form"""
    model = Order
    fields = (
        'first_name', 'last_name', 'email', 'phone', 'address1',
        'address2', 'postcode', 'city', 'country')
    template_name = 'checkout/checkout.html'
    success_url = '/'

    def get(self, request, *args, **kwargs):
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(
                request, 'There is nothing in you cart at the moment.')
            return redirect('products')
        return super().get(request, *args, **kwargs)
