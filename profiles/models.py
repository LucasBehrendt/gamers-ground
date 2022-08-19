from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """Main user profile model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    street_address_1 = models.CharField(
        max_length=80, null=True, blank=True)
    street_address_2 = models.CharField(
        max_length=80, null=True, blank=True)
    postcode = models.CharField(
        max_length=20, null=True, blank=True)
    city = models.CharField(
        max_length=40, null=True, blank=True)
    country = CountryField(
        blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username
