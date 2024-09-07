# shop/serializers.py
from rest_framework import serializers
from .models import Product, Shop, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'company', 'wholesaler_price', 'retailer_price', 'image']  # Add 'image' here

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name', 'user', 'is_wholesaler']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'retailer', 'wholesaler', 'product', 'quantity', 'total_price']
