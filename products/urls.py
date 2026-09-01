from django.urls import path
from .views import CategoryAPI, CategoryDetailAPI, ProductAPI, ProductDetailAPI

urlpatterns = [
    path('category/', CategoryAPI.as_view()),
    path('category/<int:pk>/', CategoryDetailAPI.as_view()),
    path('product/', ProductAPI.as_view()),
    path('product/<int:pk>/', ProductDetailAPI.as_view())
]
