from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import UserProfile
from products.models import Product, Category
from checkout.models import Order, OrderLineItem


class TestViews(TestCase):
    """Tests for checkout app views"""

    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user(
            username='testUser', password='testpassword', email='test@test.com'
        )

        self.user_profile = UserProfile.objects.get(
            user=self.user
        )

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

    def test_cache_checkout_data_POST(self):
        url = reverse('cache_checkout_data')
        response = self.client.post(url, {
            'client_secret': 'mock_clientsecretljksadglljsdlfj_secret'
        })

        # Can't find stripe paymentIntent, so gives 400 response
        self.assertEqual(response.status_code, 400)

    def test_checkout_page_GET(self):
        session = self.client.session
        session['cart'] = {}
        session['cart']['1'] = 1
        session.save()

        url = reverse('checkout')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    def test_checkout_page_empty_cart_GET(self):
        url = reverse('checkout')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/products/')

    def test_checkout_page_POST(self):
        session = self.client.session
        session['cart'] = {}
        session['cart']['1'] = 1
        session.save()

        url = reverse('checkout')
        response = self.client.post(url, {
            'first_name': 'test',
            'last_name': 'testson',
            'email_address': 'test@test.com',
            'phone_number': 123456789,
            'street_address_1': 'test address 1',
            'postcode': 12345,
            'city': 'testcity',
            'country': 'US',
            'client_secret': 'mock_clientsecretljksadglljsdlfj_secret'
        })

        order = Order.objects.all().first()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(order.phone_number, '123456789')
        self.assertEqual(response.url,
                         f'checkout_success/{order.order_number}')

    def test_checkout_success_page_GET(self):
        logged_in = self.client.login(
            username='testuser', password='testpassword'
        )

        session = self.client.session
        session['cart'] = {}
        session['cart']['1'] = 1
        session['save_info'] = True
        session.save()

        order = Order.objects.create(
            user_profile=self.user_profile,
            first_name='test',
            last_name='testson',
            email_address='test@test.com',
            phone_number=123456789,
            street_address_1='test address 1',
            postcode=12345,
            city='testcity',
            country='US',
        )

        OrderLineItem.objects.create(
            order=order,
            product=self.product,
            quantity=1,
        )

        url = reverse('checkout_success', args=[order.order_number])
        response = self.client.get(url)

        self.assertTrue(logged_in)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.client.session['save_info'], True)
