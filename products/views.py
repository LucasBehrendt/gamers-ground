from django.shortcuts import redirect, reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.db.models import Q
from django.db.models import Avg
from django.db.models.functions import Lower
from reviews.forms import ReviewForm
from reviews.models import Review
from .models import Product, Category


class ProductList(generic.ListView):
    """
    Renders a list of all products. Handles search queries and sorting.
    If an empty search query is posted, an error message is displayed.
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
    Renders a list of all products in a specific category.
    Handles sorting the category products.
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
    Renders a specific product detail page.
    Renders the review form and sets product to reviewed if a user already
    left a review, so user can only leave one review per product.
    """
    model = Product
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        if self.request.user.is_authenticated:
            reviewed = Review.objects.filter(
                product=product).filter(user=self.request.user)
        else:
            reviewed = False

        context['reviewed'] = reviewed
        context['form'] = self.form_class
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles review form and updates product rating.
        Redirects back to product detail page.
        """
        form = self.form_class(request.POST)
        product = self.get_object()
        if form.is_valid():
            form.instance.user = request.user
            form.instance.product = product
            form.save()

            avg_rating = Review.objects.filter(
                product=product).aggregate(Avg('rating'))['rating__avg']
            product.rating = avg_rating
            product.save()

            messages.success(request, 'Review posted. Thank You!')
            return redirect('product_detail', category=product.category,
                            slug=product.slug)
        else:
            messages.info(
                request, "Don't forget to give the product a star rating!")
            return redirect('product_detail', category=product.category,
                            slug=product.slug)


class AddProduct(LoginRequiredMixin,
                 UserPassesTestMixin,
                 generic.CreateView):
    """
    Renders add product page and checks for superuser status.
    Handles form and redirects to added product.
    """
    model = Product
    fields = ('category', 'name', 'brand', 'price', 'description', 'image')
    template_name = 'products/add_product.html'

    def form_valid(self, form):
        product = form.save()
        messages.success(self.request, 'The product was added successfully!')
        return redirect(
            reverse('product_detail', args=[product.category, product.slug]))

    def form_invalid(self, form):
        messages.error(
            self.request,
            'Failed to add product. Please check form validity.')
        return self.render_to_response(self.get_context_data(form=form))

    def test_func(self):
        return self.request.user.is_superuser


class UpdateProduct(LoginRequiredMixin,
                    UserPassesTestMixin,
                    generic.UpdateView):
    """
    Renders update product page and checks for superuser status.
    Prepoulates and handles form, and redirects to updated product.
    """
    model = Product
    fields = ('category', 'name', 'brand', 'price', 'description', 'image')
    template_name = 'products/update_product.html'

    def form_valid(self, form):
        product = form.save()
        messages.success(self.request, 'The product was updated successfully!')
        return redirect(
            reverse('product_detail', args=[product.category, product.slug]))

    def form_invalid(self, form):
        messages.error(
            self.request,
            'Failed to update product. Please check form validity.')
        return self.render_to_response(self.get_context_data(form=form))

    def test_func(self):
        return self.request.user.is_superuser


class DeleteProduct(LoginRequiredMixin,
                    UserPassesTestMixin,
                    generic.DeleteView):
    """
    Handles deleting a product through a modal.
    Checks for superuser status.
    """
    model = Product
    success_message = 'The product was deleted successfully!'
    success_url = '/products'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

    def test_func(self):
        return self.request.user.is_superuser
