from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='products'),
    path('<category>/<slug>/',
         views.ProductDetail.as_view(), name='product_detail'),
    path('add_product/', views.AddProduct.as_view(), name='add_product'),
    path('<slug>/', views.CategoryDetail.as_view(), name='category'),
]
