import stripe
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.http import JsonResponse
from django.conf import settings
from cart.context_processors import cart_contents
from .forms import OrderForm


def create_payment_intent(request):
    """Gets stripe keys and creates a payment intent"""
    stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    print(intent)

    return JsonResponse({
        'client_secret': intent.client_secret,
        'stripe_publishable_key': stripe_publishable_key,
        })


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

        if not settings.STRIPE_PUBLISHABLE_KEY:
            messages.warning(
                request, 'Stripe publishable key is missing. \
                    Did you forget to set it in your environment?')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY
        # context['client_secret'] = 'test'

        return context
