from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product, Category


class TestViews(TestCase):
    """Tests for cart app views"""

    def setUp(self):
        self.client = Client()

        self.category = Category.objects.create(
            name='Test Category',
            slug='test-category',
        )

        self.product = Product.objects.create(
            category=self.category,
            name='Test Product',
            slug='test-product',
            brand='testbrand',
            description='testdescription',
            price=123.00,
            rating=4.5,
        )

    def test_cart_page_GET(self):
        url = reverse('view_cart')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')

    def test_add_to_cart_new_item_POST(self):
        url = reverse('add_to_cart', args=[self.product.id])
        response = self.client.post(url, {
            'redirect_url': 'home'
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['cart'], {'1': 1})

    def test_add_to_cart_existing_item_POST(self):
        session = self.client.session
        session['cart'] = {}
        session['cart']['1'] = 1
        session.save()

        self.assertEqual(self.client.session['cart'], {'1': 1})

        url = reverse('add_to_cart', args=[self.product.id])
        response = self.client.post(url, {
            'redirect_url': 'home'
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['cart'], {'1': 2})

    def test_edit_cart_POST(self):
        session = self.client.session
        session['cart'] = {}
        session['cart']['1'] = 1
        session.save()

        self.assertEqual(self.client.session['cart'], {'1': 1})

        url = reverse('edit_cart', args=[self.product.id])
        response = self.client.post(url, {
            'quantity': 3
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['cart'], {'1': 3})

    def test_edit_cart_to_zero_POST(self):
        session = self.client.session
        session['cart'] = {}
        session['cart']['1'] = 1
        session.save()

        self.assertEqual(self.client.session['cart'], {'1': 1})

        url = reverse('edit_cart', args=[self.product.id])
        response = self.client.post(url, {
            'quantity': 0
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['cart'], {})

    def test_delete_from_cart_POST(self):

        session = self.client.session
        session['cart'] = {}
        session['cart']['1'] = 2
        session.save()

        self.assertEqual(self.client.session['cart'], {'1': 2})

        url = reverse('delete_from_cart', args=[self.product.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['cart'], {})
