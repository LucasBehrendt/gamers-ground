from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import UserProfile
from checkout.models import Order, OrderLineItem
from products.models import Category, Product
from reviews.models import Review
from decimal import Decimal


class TestModels(TestCase):
    """Tests for products app models"""

    def setUp(self):
        self.user = User.objects.create_user(
            username='testUser', password='testpassword', email='test@test.com'
        )

        self.user_profile = UserProfile.objects.get(
            user=self.user
        )

        self.category = Category.objects.create(
            name='Test Category',
        )

        self.product = Product.objects.create(
            category=self.category,
            name='Test Product',
            brand='testbrand',
            description='testdescription',
            price=99.00,
            # rating=4.5,
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

    def test_category_model_created(self):
        category = self.category

        self.assertEqual(category.name, 'Test Category')
        self.assertEqual(category.slug, 'test-category')

    def test_category_model_str(self):
        category = self.category

        self.assertEqual(category.__str__(), 'Test Category')

    def test_product_model_created(self):
        product = self.product

        self.assertEqual(product.category, self.category)
        self.assertEqual(product.slug, 'test-product')

    def test_product_model_str(self):
        product = self.product

        self.assertEqual(product.__str__(), 'Test Product')

    def test_product_avg_rating(self):
        product = self.product

        self.assertIsNone(product.avg_rating())

        Review.objects.create(
            user=self.user,
            product=product,
            rating=2,
            review='test review1',
        )

        self.assertEqual(product.avg_rating(), 2)

        Review.objects.create(
            user=self.user,
            product=product,
            rating=5,
            review='test review2',
        )

        self.assertEqual(product.avg_rating(), 3.5)
