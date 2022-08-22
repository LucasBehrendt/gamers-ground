from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Configuration for reviews on admin page.
    """
    list_filter = ('created_on',)
    list_display = ('user', 'product', 'rating', 'created_on')
    search_fields = ('user__username', 'rating', 'review', 'product__name')
