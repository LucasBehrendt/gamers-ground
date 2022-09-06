from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('faq/', views.FAQ.as_view(), name='faq'),
    path('terms-and-conditions/', views.TermsConditions.as_view(
        ), name='terms-and-conditions'),
    path('privacy-policy/', views.PrivacyPolicy.as_view(
        ), name='privacy-policy'),
    path('contact/', views.SendInquiry.as_view(), name='contact')
]
