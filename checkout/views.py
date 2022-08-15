from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.conf import settings
from .models import Order
from .forms import OrderForm


class Checkout(generic.CreateView):
    """Renders checkout page with payment form"""
    form_class = OrderForm
    template_name = 'checkout/checkout.html'
    success_url = '/'

    def get(self, request, *args, **kwargs):
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(
                request, 'There is nothing in you cart at the moment.')
            return redirect('products')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_public_key'] = settings.STRIPE_PUBLIC_KEY
        context['client_secret'] = 'TEST'

        return context
