from django.shortcuts import render
from django.views import generic


class Cart(generic.TemplateView):
    """Renders the cart page with saved items"""
    template_name = 'cart/cart.html'
