from django.shortcuts import render
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

class CategoryAPI(ListCreateAPIView):
    serializer_class=CategorySerializer
    queryset=Category.objects.all()

class CategoryDetailAPI(RetrieveUpdateDestroyAPIView):
    serializer_class=CategorySerializer
    queryset=Category.objects.all()

class ProductAPI(ListCreateAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()

class ProductDetailAPI(RetrieveUpdateDestroyAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()