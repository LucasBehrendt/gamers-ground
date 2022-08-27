from django.test import TestCase
from checkout.forms import OrderForm


class TestOrderForm(TestCase):
    """Tests for order form"""

    def setUp(self):
        self.form = OrderForm(data={
            'first_name': 'test',
            'last_name': 'testson',
            'email_address': 'test@test.com',
            'phone_number': 123456789,
            'street_address_1': 'test address 1',
            'postcode': 12345,
            'city': 'testcity',
            'country': 'US',
        })

    def test_order_form_valid(self):
        form = self.form

        self.assertTrue(form.is_valid())
        self.assertEqual(form.data['street_address_1'], 'test address 1')

    def test_order_form_widget(self):
        form = self.form
        form_class = form.fields['first_name'].widget.attrs['class']

        self.assertEqual(form_class, 'form-control')

    def test_order_form_invalid(self):
        form = OrderForm(data={
            'last_name': 'testson'
        })

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 7)
        self.assertEqual(form.errors['city'][0], 'This field is required.')
