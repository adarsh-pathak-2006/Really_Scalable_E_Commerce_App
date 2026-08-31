from rest_framework.serializers import ModelSerializer
from .models import Profile
from django.contrib.auth import get_user_model

User=get_user_model()

class UserGetSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'email', 'role']

class RegisterSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'email', 'role', 'password']
        write_only_fields=['password']

class ProfileSerializer(ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'
        read_only_fields=['user', 'created_on']