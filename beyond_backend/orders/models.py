from django.db import models
from django.contrib.auth import get_user_model


from products.models import Product

User = get_user_model()


class Cart(models.Model):
    productID = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product"
    )
    userID = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cart_item_user"
    )
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    def __str__(self) -> str:
        return self.productID.name


class Order(models.Model):
    userID = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="order_user"
    )
    cartItems = models.ManyToManyField(Cart)
    ordered = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    on_date = models.DateTimeField(auto_now_add=True)
    on_delivered = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Order"

    def __str__(self) -> str:
        return self.userID.email
