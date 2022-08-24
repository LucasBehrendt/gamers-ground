from django.shortcuts import render
from django.views import generic


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
