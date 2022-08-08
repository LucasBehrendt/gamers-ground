from django.shortcuts import render
from django.contrib import messages
from django.views import generic
from django.db.models import Q
from .models import Product, Category


class ProductList(generic.ListView):
    """
    Main product list view, renders a list of all products.
    """
    model = Product

    def get_queryset(self):
        query = self.request.GET.get('q')
        result = Product.objects.all()
        # if not query:
        #     messages.error(self.request, 'Please enter a search query!')
        if query:
            result = Product.objects.filter(
                Q(name__icontains=query) | Q(category__name__icontains=query) |
                Q(description__icontains=query) | Q(brand__icontains=query)
            )

        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.order_by('name')
        context['query'] = self.request.GET.get('q')

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
