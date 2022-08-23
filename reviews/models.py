from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from products.models import Product

rating_choices = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)


class Review(models.Model):
    """Main model for leaving reviews & ratings on products"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=rating_choices, default=5)
    review = models.TextField(max_length=500, null=False, blank=False)
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.user} reviewed {self.product} | Rating: {self.rating}'
