from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """Review form"""

    class Meta:
        """Definition of fields, labels & widgets used in form"""
        model = Review
        fields = ('rating', 'review')
        labels = {'review': 'Write a Review '}
        widgets = {
            'review': forms.Textarea(attrs={'rows': 5}),
        }
