from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import UserProfile


class Profile(generic.TemplateView):
    """Dispay user profile page"""
    template_name = 'profiles/profile.html'
