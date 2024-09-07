from django.urls import path
from . import views

urlpatterns = [
    path('api/products/', views.product_list, name='product_list'),
    path('api/shops/', views.shop_list, name='shop_list'),
    path('api/orders/', views.order_list, name='order_list'),
]
