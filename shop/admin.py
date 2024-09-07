from django.contrib import admin
from .models import User, Category, Company, Product, Shop, Order

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'wholesaler_price', 'retailer_price')

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'is_wholesaler')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('retailer', 'wholesaler', 'product', 'quantity', 'total_price')
