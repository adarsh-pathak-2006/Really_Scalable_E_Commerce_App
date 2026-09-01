from django.urls import path
from .views import MyCartAPI, CartItemAPI, AddToCartAPI, IndividualCartItem

urlpatterns = [
    path('my-cart/', MyCartAPI.as_view()),
    path("cart-items/", CartItemAPI.as_view()),
    path('cart-add/', AddToCartAPI.as_view()),
    path('my-cart/<int:pk>/', IndividualCartItem.as_view()),
]
