from rest_framework.serializers import ModelSerializer
from authentication.serializers import ProfileSerializer
from .models import Cart, CartItem
from products.serializers import ProductSerializer

class CartSerializer(ModelSerializer):
    user=ProfileSerializer(read_only=True)
    class Meta:
        model=Cart
        fields='__all__'
        read_only_fields=['id', 'user', 'created_at']

class CartItemSerializer(ModelSerializer):
    cart=CartSerializer(read_only=True)
    item=ProductSerializer(read_only=True)
    class Meta:
        model=CartItem
        fields='__all__'
        read_only_fields=['added_on']
