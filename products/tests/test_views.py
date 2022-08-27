from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import UserProfile
from products.models import Product, Category
from reviews.models import Review


class TestViews(TestCase):
    """Tests for products app views"""

    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user(
            username='testUser', password='testpassword', email='test@test.com'
        )

        self.super_user = User.objects.create_superuser(
            username='testSuperUser', password='testsuperpassword',
            email='testSuper@test.com'
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
        )

    def test_product_list_GET(self):
        url = reverse('products')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_list.html')

    def test_product_list_sort_GET(self):
        url = reverse('products')
        response = self.client.get(url, {
            'sort': 'name',
            'direction': 'desc',
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_list.html')
        self.assertEqual(response.context['current_sorting'], 'name_desc')

    def test_product_list_query_GET(self):
        url = reverse('products')
        response = self.client.get(url, {
            'q': 'razer'
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_list.html')
        self.assertEqual(response.context['query'], 'razer')

    def test_category_products_GET(self):
        url = reverse('category', args=['test-category'])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/category_detail.html')

    def test_non_existing_category_products_404_GET(self):
        url = reverse('category', args=['non-existing-category'])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_category_products_sort_GET(self):
        url = reverse('category', args=['test-category'])
        response = self.client.get(url, {
            'sort': 'name',
            'direction': 'desc',
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/category_detail.html')
        self.assertEqual(response.context['current_sorting'], 'name_desc')

    def test_product_detail_GET(self):
        url = reverse('product_detail', args=['test-category', 'test-product'])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_non_existing_product_detail_GET(self):
        url = reverse('product_detail',
                      args=['test-category', 'non-existing-product'])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_review_product(self):
        logged_in = self.client.login(
            username='testuser', password='testpassword'
        )

        url = reverse('product_detail', args=['test-category', 'test-product'])
        response = self.client.post(url, {
            'rating': 3,
            'review': 'test review'
        })

        review = Review.objects.get(id=1)

        self.assertTrue(logged_in)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(review.rating, 3)
        self.assertEqual(review.review, 'test review')

    def test_add_product_as_regular_user_GET(self):
        logged_in = self.client.login(
            username='testUser', password='testpassword'
        )

        url = reverse('add_product')
        response = self.client.get(url)

        self.assertTrue(logged_in)
        # Forbidden for users without superuser status
        self.assertEqual(response.status_code, 403)

    def test_add_product_as_super_user_GET(self):
        logged_in = self.client.login(
            username='testSuperUser', password='testsuperpassword'
        )

        url = reverse('add_product')
        response = self.client.get(url)

        self.assertTrue(logged_in)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_add_product_as_super_user_POST(self):
        logged_in = self.client.login(
            username='testSuperUser', password='testsuperpassword'
        )

        url = reverse('add_product')
        response = self.client.post(url, {
            'category': 1,
            'name': 'Test Add Product',
            'brand': 'Brand',
            'price': 79,
            'description': 'Description Added Product',
        })

        product = Product.objects.get(id=2)

        self.assertTrue(logged_in)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(product.name, 'Test Add Product')
        self.assertEqual(product.price, 79)

    def test_update_product_as_regular_user_GET(self):
        logged_in = self.client.login(
            username='testUser', password='testpassword'
        )

        url = reverse('update_product', args=['test-product'])
        response = self.client.get(url)

        self.assertTrue(logged_in)
        # Forbidden for users without superuser status
        self.assertEqual(response.status_code, 403)

    def test_update_product_as_super_user_GET(self):
        logged_in = self.client.login(
            username='testSuperUser', password='testsuperpassword'
        )

        url = reverse('update_product', args=['test-product'])
        response = self.client.get(url)

        self.assertTrue(logged_in)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/update_product.html')

    def test_update_product_as_super_user_POST(self):
        logged_in = self.client.login(
            username='testSuperUser', password='testsuperpassword'
        )

        url = reverse('update_product', args=['test-product'])
        response = self.client.post(url, {
            'category': 1,
            'name': 'Test Update Product',
            'brand': 'Brand',
            'price': 790,
            'description': 'Description Updated Product',
        })

        product = Product.objects.get(id=1)

        self.assertTrue(logged_in)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(product.name, 'Test Update Product')
        self.assertEqual(product.price, 790)

    def test_delete_product_as_regular_user_POST(self):
        logged_in = self.client.login(
            username='testUser', password='testpassword'
        )

        url = reverse('delete_product', args=['test-product'])
        response = self.client.post(url)

        products = Product.objects.all()

        self.assertTrue(logged_in)
        # Product still exists
        self.assertEqual(products.first().name, 'Test Product')
        # Forbidden for users without superuser status
        self.assertEqual(response.status_code, 403)

    def test_delete_product_as_super_user_POST(self):
        logged_in = self.client.login(
            username='testSuperUser', password='testsuperpassword'
        )

        url = reverse('delete_product', args=['test-product'])
        response = self.client.post(url)

        products = Product.objects.all()

        self.assertTrue(logged_in)
        self.assertEqual(response.status_code, 302)
        self.assertQuerysetEqual(products, [])
