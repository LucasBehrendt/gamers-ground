from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewCart.as_view(), name='view_cart'),
]
