from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from profiles.models import UserProfile
from .models import Inquiry
from .forms import InquiryForm


class Home(generic.TemplateView):
    """Renders the home page"""
    template_name = 'home/index.html'


class TermsConditions(generic.TemplateView):
    """Renders the terms & conditions page"""
    template_name = 'home/terms-and-conditions.html'


class PrivacyPolicy(generic.TemplateView):
    """Renders the privacy policy page"""
    template_name = 'home/privacy-policy.html'


class FAQ(generic.TemplateView):
    """Renders the privacy policy page"""
    template_name = 'home/faq.html'


class SendInquiry(SuccessMessageMixin, generic.CreateView):
    """
    Renders the contact page with inquiry form
    """
    model = Inquiry
    template_name = 'home/contact.html'
    form_class = InquiryForm
    success_message = (
        'Your inquiry has been sent and a \
        copy was sent to you. Thank you!'
    )
    success_url = '/'

    def get_initial(self):
        # If user is signed in, get profile info & set as initial values
        if self.request.user.is_authenticated:
            profile = get_object_or_404(UserProfile, user=self.request.user)
            return {
                'first_name': profile.user.get_short_name(),
                'last_name': profile.get_last_name(),
                'email_address': profile.user.email,
                'phone_number': profile.phone_number,
            }
