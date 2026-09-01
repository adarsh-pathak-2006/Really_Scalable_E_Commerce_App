from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, ProfileSerializer
from .models import Profile
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from orders.models import Cart

User=get_user_model()

class RegisterAPI(APIView):
    def post(self, request):
        serial=RegisterSerializer(data=request.data)
        if serial.is_valid():
            username=serial.validated_data['username']
            email=serial.validated_data['email']
            password=serial.validated_data['password']
            role=serial.validated_data['role']

            if User.objects.filter(Q(username=username) | Q(email=email)).exists():
                return Response({'message':'username or email already exists'}, status=400)
            user=User.objects.create_user(username=username, email=email, password=password, role=role)
            profile_data=Profile.objects.create(user=user)
            Cart.objects.create(user=profile_data)
            return Response({'message':'user registration successfull'}, status=201)
        return Response(serial.errors, status=400)

class MyProfileAPI(RetrieveUpdateDestroyAPIView):
    serializer_class=ProfileSerializer

    def get_object(self):
        return get_object_or_404(Profile.objects.select_related('user'), user__id=self.request.user.id)
