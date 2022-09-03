from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """Order form configuration"""

    class Meta:
        """Definition of fields, labels & widgets used in form"""
        model = Order
        fields = (
            'first_name', 'last_name', 'email_address',
            'phone_number', 'street_address_1', 'street_address_2',
            'postcode', 'city', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            if field != 'country':
                if self.fields[field].required:
                    self.fields[field].widget.attrs[
                        'placeholder'] = self.fields[field].label + ' *'
                else:
                    self.fields[field].widget.attrs[
                        'placeholder'] = self.fields[field].label
