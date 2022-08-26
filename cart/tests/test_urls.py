from django.test import TestCase
from django.urls import reverse, resolve
from cart import views


class TestUrls(TestCase):
    """Tests for cart app urls"""

    def test_cart_url(self):
        url = reverse('view_cart')
        self.assertEqual(resolve(url).func.view_class, views.ViewCart)

    def test_add_to_cart_url(self):
        url = reverse('add_to_cart', args=[1])
        self.assertEqual(resolve(url).func.view_class, views.AddToCart)

    def test_edit_cart_url(self):
        url = reverse('edit_cart', args=[1])
        self.assertEqual(resolve(url).func.view_class, views.EditCart)

    def test_delete_from_cart_url(self):
        url = reverse('delete_from_cart', args=[1])
        self.assertEqual(resolve(url).func.view_class, views.DeleteFromCart)
