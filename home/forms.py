from django import forms
from .models import Inquiry


class InquiryForm(forms.ModelForm):
    """Inquiry form configuration"""

    class Meta:
        """Definition of fields, labels & widgets used in form"""
        model = Inquiry
        exclude = ('created_on',)
        widgets = {
            'inquiry': forms.Textarea(attrs={'rows': 7}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            if self.fields[field].required:
                self.fields[field].widget.attrs[
                    'placeholder'] = self.fields[field].label + ' *'
            else:
                self.fields[field].widget.attrs[
                    'placeholder'] = self.fields[field].label
