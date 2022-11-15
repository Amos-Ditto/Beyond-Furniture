from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250)
    categoryID = models.ForeignKey(
        Categories, on_delete=models.CASCADE, related_name="category"
    )
    description = models.TextField(null=True, blank=True)
    currentPrice = models.FloatField()
    previousPrice = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self) -> str:
        return self.name
