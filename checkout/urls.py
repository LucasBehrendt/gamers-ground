from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.Checkout.as_view(), name='checkout'),
    path('checkout_success/<order_number>/', views.CheckoutSuccess.as_view(
        ), name='checkout_success'),
    path('secret/', views.create_payment_intent, name='stripe_secret'),
    path('webhook/', webhook, name='webhook'),
]
