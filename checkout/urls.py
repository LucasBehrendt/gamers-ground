from django.urls import path
from . import views

urlpatterns = [
    path('', views.Checkout.as_view(), name='checkout'),
    path('secret/', views.create_payment_intent, name='stripe_secret'),
]
