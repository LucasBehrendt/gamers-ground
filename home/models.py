from django.db import models
from django.utils import timezone


class Inquiry(models.Model):
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    email_address = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    inquiry = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Inquiries'

    def __str__(self):
        return f'Inquiry from: {self.email_address}'
