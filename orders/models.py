from django.db import models
from authentication.models import Profile
from products.models import Product

class Cart(models.Model):
    user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.user.username


class CartItem(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    item=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    added_on=models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.item.stock < self.quantity:
            raise ValueError("Cannot add product quantity more the stock avaliable.")
        if not self.item.is_avaliable:
            raise ValueError("item is out of stock.")
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.item.name