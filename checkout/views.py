import json
import stripe
from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.views.decorators.http import require_POST
from django.views import generic
from django.contrib import messages
from django.http import JsonResponse
from django.conf import settings
from cart.context_processors import cart_contents
from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserDeliveryForm
from .models import Order, OrderLineItem
from .forms import OrderForm


@require_POST
def cache_checkout_data(request):
    """
    Modify payment intent with metadata.
    Taken from Boutique Ado walkthrough project.
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request,
            'Sorry, your payment cannot be processed right now.\
            Please try again later.'
        )
        return HttpResponse(content=e, status=400)


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
        order = form.save(commit=False)
        pid = self.request.POST.get('client_secret').split('_secret')[0]
        order.stripe_pid = pid
        order.save()
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

    def get_initial(self):
        # If user is signed in, get profile info & set as initial values
        if self.request.user.is_authenticated:
            profile = get_object_or_404(UserProfile, user=self.request.user)
            return {
                'first_name': profile.user.get_short_name(),
                'last_name': profile.get_last_name(),
                'email_address': profile.user.email,
                'phone_number': profile.phone_number,
                'street_address_1': profile.street_address_1,
                'street_address_2': profile.street_address_2,
                'postcode': profile.postcode,
                'city': profile.city,
                'country': profile.country,
            }

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


class CheckoutSuccess(generic.View):
    """Renders checkout success page with order details"""

    def get(self, request, order_number):
        save_info = request.session.get('save_info')
        order = get_object_or_404(Order, order_number=order_number)

        # If user is signed in, their profile is assigned to the order
        if request.user.is_authenticated:
            profile = get_object_or_404(UserProfile, user=request.user)
            order.user_profile = profile
            order.save()

            # Stores user info if save info box is checked
            if save_info:
                delivery_data = {
                    'phone_number': order.phone_number,
                    'street_address_1': order.street_address_1,
                    'street_address_2': order.street_address_2,
                    'postcode': order.postcode,
                    'city': order.city,
                    'country': order.country,
                }
                delivery_form = UserDeliveryForm(
                    delivery_data, instance=profile)
                if delivery_form.is_valid():
                    delivery_form.save()

        messages.success(
            request, 'Your order has been successfully processed.\
                Thank you for shopping with us!')

        if 'cart' in request.session:
            del request.session['cart']

        context = {
            'order': order,
        }

        template_name = 'checkout/checkout_success.html'
        return render(request, template_name, context)
