from django.test import TestCase
from django.urls import reverse, resolve
from checkout import views
from checkout.webhooks import webhook


class TestUrls(TestCase):
    """Tests for checkout app urls"""

    def test_checkout_url(self):
        url = reverse('checkout')
        self.assertEqual(resolve(url).func.view_class, views.Checkout)

    def test_checkout_success_url(self):
        url = reverse('checkout_success',
                      args=['ltrhwi46mu7231n3vcf5k67l88jfds5l'])
        self.assertEqual(resolve(url).func.view_class, views.CheckoutSuccess)

    def test_stripe_secret_url(self):
        url = reverse('stripe_secret')
        self.assertEqual(resolve(url).func, views.create_payment_intent)

    def test_webhook_url(self):
        url = reverse('webhook')
        self.assertEqual(resolve(url).func, webhook)

    def test_cache_checkout_data_url(self):
        url = reverse('cache_checkout_data')
        self.assertEqual(resolve(url).func, views.cache_checkout_data)
