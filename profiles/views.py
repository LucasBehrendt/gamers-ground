from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import DeleteView
from checkout.models import Order
from .models import UserProfile
from .forms import UserDetailsForm, UserDeliveryForm


@login_required
def profile(request):
    """
    Renders user profile page with details and delivery form prepopulated.
    Shows order history and handles updating user profile info.
    """
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
    else:
        details_form = UserDetailsForm(instance=request.user)
        delivery_form = UserDeliveryForm(instance=profile)
    orders = profile.orders.all().order_by('-date')

    context = {
        'details_form': details_form,
        'delivery_form': delivery_form,
        'orders': orders,
    }

    template = 'profiles/profile.html'
    return render(request, template, context)


def order_history(request, order_number):
    """
    Uses checkout success page for rendering order history details.
    Passes history context to template to allow repurposing it.
    """
    order = get_object_or_404(Order, order_number=order_number)

    context = {
        'order': order,
        'history': True,
    }

    template = 'checkout/checkout_success.html'
    return render(request, template, context)


class DeleteUser(LoginRequiredMixin,
                 UserPassesTestMixin,
                 DeleteView):
    """
    Handles deleting a signed in users account through a modal.
    Validates that the user equals the request.user.
    """
    model = User
    success_message = 'Your account has been deleted!'
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteUser, self).delete(request, *args, **kwargs)

    def test_func(self):
        user = self.get_object()
        return self.request.user == user
