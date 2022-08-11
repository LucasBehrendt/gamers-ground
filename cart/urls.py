from django.urls import path
from . import views

urlpatterns = [
    path('', views.ViewCart.as_view(), name='view_cart'),
    path('add/<item_id>/', views.AddToCart.as_view(), name='add_to_cart'),
    path('edit/<item_id>/', views.EditCart.as_view(), name='edit_cart'),
]
