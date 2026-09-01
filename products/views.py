from django.shortcuts import render
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from e_commerce_backend.pagination import GeneralPagination
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)

class CategoryAPI(ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class=CategorySerializer
    queryset=Category.objects.all()
    pagination_class=GeneralPagination

    @method_decorator(cache_page(60*5))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class CategoryDetailAPI(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class=CategorySerializer
    queryset=Category.objects.all()

    @method_decorator(cache_page(60*5))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ProductAPI(ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class=ProductSerializer
    queryset=Product.objects.select_related('category')
    pagination_class=GeneralPagination

    @method_decorator(cache_page(60*5))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ProductDetailAPI(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class=ProductSerializer
    queryset=Product.objects.select_related('category')

    @method_decorator(cache_page(60*5))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)