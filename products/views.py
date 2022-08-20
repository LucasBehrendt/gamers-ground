from django.shortcuts import render
from django.contrib import messages
from django.views import generic
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
# from .forms import AddProductForm


class ProductList(generic.ListView):
    """
    Main product list view, renders a list of products.
    Also handles searches and sorting.
    """
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        products = Product.objects.all()
        query = None
        sort = None
        direction = None

        if 'sort' in self.request.GET:
            sortkey = self.request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in self.request.GET:
                direction = self.request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'q' in self.request.GET:
            query = self.request.GET['q']
            if not query:
                messages.error(self.request, 'Please enter a search query!')
            products = products.filter(
                Q(name__icontains=query) | Q(category__name__icontains=query) |
                Q(description__icontains=query) | Q(brand__icontains=query)
            )
        context['current_sorting'] = f'{sort}_{direction}'
        context['query'] = query
        context['object_list'] = products
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

        category = self.get_object()
        cat_products = category.products.all()
        sort = None
        direction = None

        if 'sort' in self.request.GET:
            sortkey = self.request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                cat_products = cat_products.annotate(lower_name=Lower('name'))
            if 'direction' in self.request.GET:
                direction = self.request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            cat_products = cat_products.order_by(sortkey)
        context['current_sorting'] = f'{sort}_{direction}'
        context['cat_products'] = cat_products

        context['categories'] = Category.objects.order_by('name')
        context['current_slug'] = category.slug
        return context


class ProductDetail(generic.DetailView):
    """
    Main product detail view, renders a specific product.
    """
    model = Product


class AddProduct(generic.CreateView):
    """
    View for creating products
    """
    # form_class = AddProductForm
    model = Product
    fields = '__all__'
    template_name = 'products/add_product.html'
    success_message = 'The product was added successfully!'
    success_url = '/products/{category}/{slug}'
