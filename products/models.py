from django.db import models
from django.db.models import Avg
from django.template.defaultfilters import slugify
from reviews.models import Review


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
        """
        Overrides save method and sets slug field to
        slugified name.
        """
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Product(models.Model):
    """
    Main model for products listed on the store.
    Rating field is automatically updated when reviews for
    the product are posted or deleted.
    """
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254)
    brand = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=3, decimal_places=2, null=True, blank=True)

    def avg_rating(self):
        """
        Returns the average rating of a product by aggregating
        rating field on review model.
        """
        avg = Review.objects.filter(
            product=self).aggregate(Avg('rating'))['rating__avg']
        return avg

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Overrides save method and sets slug field to
        slugified name.
        """
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
