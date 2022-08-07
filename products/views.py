from django.shortcuts import render
from django.views import generic
from .models import Product, Category


class ProductList(generic.ListView):
    """
    Main product list view, renders a list of all products.
    """
    model = Product


class ProductDetail(generic.DetailView):
    """
    Main product detail view, renders a specific product.
    """
    model = Product
