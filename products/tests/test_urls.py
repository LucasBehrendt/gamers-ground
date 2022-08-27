from django.test import TestCase
from django.urls import reverse, resolve
from products import views


class TestUrls(TestCase):
    """Tests for products app urls"""

    def test_products_url(self):
        url = reverse('products')
        self.assertEqual(resolve(url).func.view_class, views.ProductList)

    def test_add_product_url(self):
        url = reverse('add_product')
        self.assertEqual(resolve(url).func.view_class, views.AddProduct)

    def test_update_product_url(self):
        url = reverse('update_product', args=['productslug'])
        self.assertEqual(resolve(url).func.view_class, views.UpdateProduct)

    def test_delete_product_url(self):
        url = reverse('delete_product', args=['productslug'])
        self.assertEqual(resolve(url).func.view_class, views.DeleteProduct)

    def test_category_products_url(self):
        url = reverse('category', args=['categoryslug'])
        self.assertEqual(resolve(url).func.view_class, views.CategoryDetail)

    def test_product_detail_url(self):
        url = reverse('product_detail', args=['categoryslug', 'productslug'])
        self.assertEqual(resolve(url).func.view_class, views.ProductDetail)
