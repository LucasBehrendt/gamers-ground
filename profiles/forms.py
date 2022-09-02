from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserDetailsForm(forms.ModelForm):
    """User details configuration"""

    class Meta:
        """Definition of fields used in form"""
        model = User
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs[
                    'placeholder'] = self.fields[field].label


class UserDeliveryForm(forms.ModelForm):
    """Order form configuration"""

    class Meta:
        """Definition of fields used in form"""
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            if field != 'country':
                self.fields[field].widget.attrs[
                            'placeholder'] = self.fields[field].label
            self.fields['country'].widget.attrs['id'] = 'default_country'
