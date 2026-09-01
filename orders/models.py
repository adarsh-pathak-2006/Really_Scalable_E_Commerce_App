from django.db import models
from authentication.models import Profile
from products.models import Product

class Cart(models.Model):
    user=models.OneToOneField(Profile, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.user.username


class CartItem(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    item=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    added_on=models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints=[models.UniqueConstraint(fields=['cart', 'item'], name='unique_item_per_cart_constraint')]

    def __str__(self):
        return self.item.name

