from django.shortcuts import render
from django.views import generic


class Home(generic.TemplateView):
    """Renders the home page"""
    template_name = 'home/index.html'
