from django.urls import path
from .views import RegisterAPI, MyProfileAPI
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterAPI.as_view()),
    path('my-profile/', MyProfileAPI.as_view()),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
