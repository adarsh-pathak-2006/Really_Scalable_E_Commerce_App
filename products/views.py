from django.shortcuts import render
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from e_commerce_backend.pagination import GeneralPagination
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class CategoryAPI(ListCreateAPIView):
    serializer_class=CategorySerializer
    queryset=Category.objects.all()
    pagination_class=GeneralPagination

    @method_decorator(cache_page(60*5))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class CategoryDetailAPI(RetrieveUpdateDestroyAPIView):
    serializer_class=CategorySerializer
    queryset=Category.objects.all()

    @method_decorator(cache_page(60*5))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ProductAPI(ListCreateAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    pagination_class=GeneralPagination

    @method_decorator(cache_page(60*5))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ProductDetailAPI(RetrieveUpdateDestroyAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()

    @method_decorator(cache_page(60*5))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)