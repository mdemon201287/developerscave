from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ShopViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'shops', ShopViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
