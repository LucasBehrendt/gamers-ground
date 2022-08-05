from django.shortcuts import render
from django.views import generic
from .models import Product


class ProductList(generic.ListView):
    """
    Main product list view, renders a list of all products.
    """
    model = Product
