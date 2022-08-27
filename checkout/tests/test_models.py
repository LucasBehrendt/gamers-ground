from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import UserProfile
from checkout.models import Order, OrderLineItem
from products.models import Category, Product
from decimal import Decimal


class TestModels(TestCase):
    """Tests for checkout app models"""

    def setUp(self):
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
            price=99.00,
            rating=4.5,
        )

        self.order = Order.objects.create(
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

        self.line_item = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=1,
        )

    def test_order_model_created(self):
        order = self.order

        self.assertEqual(order.first_name, 'test')
        self.assertEqual(order.city, 'testcity')
        self.assertEqual(order.street_address_2, None)

    def test_order_model_order_number_generated_and_returned_str(self):
        order = self.order

        self.assertEqual(len(order.order_number), 32)
        self.assertEqual(order.__str__(), order.order_number)

    def test_order_model_delivery_cost(self):
        order = self.order

        self.assertEqual(order.delivery_cost, Decimal('7.99'))

    def test_order_model_free_delivery(self):
        OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=1,
        )

        order = self.order

        self.assertEqual(order.delivery_cost, 0)
        self.assertEqual(order.order_total, 198)

    def test_order_model_update_total(self):
        order = self.order

        self.assertEqual(order.order_total, 99)
        self.assertEqual(order.grand_total, Decimal('106.99'))

    def test_line_item_str(self):
        line_item = self.line_item

        self.assertEqual(line_item.__str__(), 'testbrand Test Product')

    def test_line_item_total(self):
        line_item2 = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=3,
        )

        self.assertEqual(line_item2.quantity, 3)
        self.assertEqual(line_item2.lineitem_total, 297)
