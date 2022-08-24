from django.urls import path
from . import views

urlpatterns = [
    path('delete_review/<int:review_id>', views.DeleteReview.as_view(
        ), name='delete_review'),
]
