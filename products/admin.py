from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Configuration for Categories on admin page.
    """
    list_display = ('name', 'slug')
    ordering = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Configuration for Products on admin page.
    """
    list_display = ('name', 'category', 'brand', 'price')
    list_filter = ('brand', 'category__name')
    search_fields = ('name', 'category', 'brand')
    ordering = ('name',)
