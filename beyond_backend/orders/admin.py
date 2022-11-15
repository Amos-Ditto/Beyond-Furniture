from django.contrib import admin

from .models import Order, Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["id", "productID", "userID", "quantity", "ordered"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "userID", "ordered", "delivered", "on_date", "on_delivered"]
