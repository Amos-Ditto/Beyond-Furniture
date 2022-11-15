from django.contrib import admin
from .models import Categories, Product


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "categoryID", "currentPrice", "previousPrice"]
