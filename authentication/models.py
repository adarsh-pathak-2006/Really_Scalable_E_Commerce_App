from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES=[('CUSTOMER', 'Customer'), ('ADMIN', 'Admin')]
    role=models.CharField(max_length=10, choices=ROLE_CHOICES, default='CUSTOMER')


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username