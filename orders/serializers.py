from rest_framework.serializers import ModelSerializer
from authentication.serializers import UserGetSerializer
from .models import Cart, CartItem, Order


class CartSerializer(ModelSerializer):
    class Meta:
        model=Cart
        fields='__all__'
        read_only_fields='__all__'

class CartItemSerializer(ModelSerializer):
    class Meta:
        model=CartItem
        fields='__all__'
        read_only_fields=['cart', 'item', 'added_on']

class OrderSerializer(ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'
        read_only_fields=['cart', 'created_on']