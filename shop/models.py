# shop/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('admin', 'Admin'),
        ('wholesaler', 'Wholesaler'),
        ('retailer', 'Retailer'),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='companies')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='products')
    wholesaler_price = models.DecimalField(max_digits=10, decimal_places=2)
    retailer_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)  # Add this line

    def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='shop')
    is_wholesaler = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Order(models.Model):
    retailer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'retailer'}, related_name='orders_placed')
    wholesaler = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'wholesaler'}, related_name='orders_received')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total_price = self.product.wholesaler_price * self.quantity
        super().save(*args, **kwargs)
