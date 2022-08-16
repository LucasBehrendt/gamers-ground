import stripe
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.http import JsonResponse
from django.conf import settings
from cart.context_processors import cart_contents
from products.models import Product
from .models import Order, OrderLineItem
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

    return JsonResponse({
        'client_secret': intent.client_secret,
        'stripe_publishable_key': stripe_publishable_key,
        })


class Checkout(generic.CreateView):
    """Renders checkout page with payment form"""
    form_class = OrderForm
    template_name = 'checkout/checkout.html'
    success_url = 'checkout_success/{order_number}'

    def form_valid(self, form):
        cart = self.request.session.get('cart', {})
        order = form.save()
        for item_id, quantity in cart.items():
            try:
                product = get_object_or_404(Product, pk=item_id)
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity,
                )
                order_line_item.save()
            except Product.DoesNotExist:
                messages.error(
                    self.request,
                    'One of the product in your cart was not \
                        found in our database. Please get in \
                            touch with us and we will help!')
                order.delete()
                return redirect(reverse('view_cart'))

        self.request.session['save_info'] = 'save-info' in self.request.POST

        return super().form_valid(form)

    # add form_invalid ??

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


class CheckoutSuccess(generic.View):
    """Renders checkout success page with order details"""

    def get(self, request, order_number):
        save_info = request.session.get('save_info')
        order = get_object_or_404(Order, order_number=order_number)
        # messages.success(
        #     request, f'Your order has been successfully processed.\
        #         Thank you for shopping with us! A confirmation email was sent\
        #         to {order.email_address}. Order number: {order_number}')

        if 'cart' in request.session:
            del request.session['cart']

        context = {
            'order': order,
        }

        template_name = 'checkout/checkout_success.html'
        return render(request, template_name, context)
