from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Configuration for Categories on admin page.
    """
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')
    ordering = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Configuration for Products on admin page.
    """
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'rating', 'category', 'brand', 'price')
    list_filter = ('brand', 'rating', 'category__name')
    search_fields = ('name', 'rating', 'category__name', 'brand')
    ordering = ('name',)
