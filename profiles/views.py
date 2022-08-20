from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from checkout.models import Order
from .models import UserProfile
from .forms import UserDetailsForm, UserDeliveryForm


def profile(request):
    """user profiles"""
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        details_form = UserDetailsForm(request.POST, instance=request.user)
        delivery_form = UserDeliveryForm(request.POST, instance=profile)
        # Handle both forms in one post request
        # source: https://stackoverflow.com/questions/27832076/
        if all((details_form.is_valid(), delivery_form.is_valid())):
            details = details_form.save()
            delivery = delivery_form.save(commit=False)
            delivery.user = details
            delivery.save()
            messages.success(request, 'Your profile has been updated!')

    orders = profile.orders.all().order_by('-date')
    details_form = UserDetailsForm(instance=request.user)
    delivery_form = UserDeliveryForm(instance=profile)

    context = {
        'details_form': details_form,
        'delivery_form': delivery_form,
        'orders': orders,
    }

    template = 'profiles/profile.html'
    return render(request, template, context)


def order_history(request, order_number):
    """Render details for past order"""
    order = get_object_or_404(Order, order_number=order_number)

    context = {
        'order': order,
        'history': True,
    }

    template = 'checkout/checkout_success.html'
    return render(request, template, context)
