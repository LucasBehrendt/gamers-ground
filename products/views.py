from django.shortcuts import render
from django.views import generic
from .models import Product, Category


class ProductList(generic.ListView):
    """
    Main product list view, renders a list of all products.
    """
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.order_by('name')

        return context


class CategoryDetail(generic.DetailView):
    """
    Main category list view, renders a list
    of all products in a specific category.
    """
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.order_by('name')
        current = self.get_object()
        context['current_slug'] = current.slug

        return context


class ProductDetail(generic.DetailView):
    """
    Main product detail view, renders a specific product.
    """
    model = Product
