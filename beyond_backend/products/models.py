import os
import random
from django.db import models


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = "{new_filename}{ext}".format(new_filename=new_filename, ext=ext)
    return "products/{final_filename}".format(final_filename=final_filename)


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
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self) -> str:
        return self.name
