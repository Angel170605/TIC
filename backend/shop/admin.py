from django.contrib import admin
from .models import Product, Cart, CartProduct

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'stock_img', 'stock', 'slug']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'price']

@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'cart', 'quantity', 'description', 'input_text', 'input_image']