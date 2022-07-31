from django.shortcuts import render
from django.views import generic


class Home(generic.TemplateView):
    """Home page"""
    template_name = 'home/index.html'
