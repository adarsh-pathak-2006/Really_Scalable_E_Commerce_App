from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Category, Product

class CategorySerializer(ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class ProductSerializer(ModelSerializer):
    category=PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model=Product
        fields='__all__'
        read_only_fields=['is_available']