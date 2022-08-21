from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    """
    Main model for each available category.
    """
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Product(models.Model):
    """
    Main model for products listed on the store.
    """
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254)
    brand = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
