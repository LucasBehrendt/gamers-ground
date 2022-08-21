from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='products'),
    path('add_product/', views.AddProduct.as_view(), name='add_product'),
    path('update_product/<slug>/', views.UpdateProduct.as_view(
        ), name='update_product'),
    path('delete_product/<slug>/', views.DeleteProduct.as_view(
        ), name='delete_product'),
    path('<slug>/', views.CategoryDetail.as_view(), name='category'),
    path('<category>/<slug>/', views.ProductDetail.as_view(
        ), name='product_detail'),
]
