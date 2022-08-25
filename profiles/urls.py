from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('delete_user/<int:pk>', views.DeleteUser.as_view(
        ), name='delete_user'),
    path('order_history/<order_number>/',
         views.order_history, name="order_history")
]
