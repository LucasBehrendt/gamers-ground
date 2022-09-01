from django.shortcuts import redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Avg
from .models import Review


class DeleteReview(LoginRequiredMixin, generic.View):
    """View for users deleting own reviews"""
    def post(self, request, review_id):
        review = get_object_or_404(Review, pk=review_id)
        product = review.product
        review.delete()

        avg_rating = Review.objects.filter(
                product=product).aggregate(Avg('rating'))['rating__avg']
        product.rating = avg_rating
        product.save()

        messages.success(request, 'Your review has been deleted!')

        return redirect('product_detail', category=product.category,
                        slug=product.slug)
