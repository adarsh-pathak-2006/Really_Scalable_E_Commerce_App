from django.shortcuts import get_object_or_404
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from e_commerce_backend.pagination import GeneralPagination
from products.models import Product

class MyCartAPI(RetrieveAPIView):
    serializer_class=CartSerializer

    def get_object(self):
        return Cart.objects.select_related('user__user').get(user__user=self.request.user)

class CartItemAPI(APIView):
    def get(self, request):
        queryset=CartItem.objects.select_related('cart__user__user', 'item').filter(cart__user__user=request.user)
        paginator=GeneralPagination()
        page=paginator.paginate_queryset(queryset, request, view=self)
        serial=CartItemSerializer(page, many=True)
        return paginator.get_paginated_response(serial.data)

class AddToCartAPI(APIView):
    def post(self, request, pk):
        serial=CartItemSerializer(data=request.data)
        if serial.is_valid():
            quantity=serial.validated_data['quantity']
            product_data=get_object_or_404(Product, id=pk)
            cart_data=get_object_or_404(Cart.objects.select_related('user__user'), user__user=request.user)
            CartItem.objects.create(cart=cart_data, item=product_data, quantity=quantity)
            return Response({'message':'item successfully added in the cart'}, status=201)
        return Response(serial.errors, status=400)

class IndividualCartItem(APIView):
    def get(self, request, pk):
        data=get_object_or_404(CartItem.objects.select_related('cart__user__user'), cart__user__user=request.user, id=pk)
        serial=CartItemSerializer(data)
        return Response(serial.data, status=200)

    def patch(self, request, pk):
        instance=get_object_or_404(CartItem.objects.select_related('cart__user__user'), cart__user__user=request.user, id=pk)
        serial=CartItemSerializer(instance, data=request.data, partial=True)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=200)
        return Response(serial.errors, status=400)

    def delete(self, request, pk):
        instance=get_object_or_404(CartItem.objects.select_related('cart__user__user'), cart__user__user=request.user, id=pk)
        instance.delete()
        return Response(status=204)
        