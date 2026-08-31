from rest_framework.serializers import ModelSerializer
from authentication.serializers import UserGetSerializer
from .models import Cart, CartItem, Order
from products.serializers import ProductSerializer

class CartSerializer(ModelSerializer):
    user=UserGetSerializer(read_only=True)
    class Meta:
        model=Cart
        fields='__all__'
        read_only_fields='__all__'

class CartItemSerializer(ModelSerializer):
    cart=CartSerializer(read_only=True)
    item=ProductSerializer(read_only=True)
    class Meta:
        model=CartItem
        fields='__all__'
        read_only_fields=['added_on']

class OrderSerializer(ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'
        read_only_fields=['cart', 'created_on']