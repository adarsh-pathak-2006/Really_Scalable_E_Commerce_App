from django.urls import path
from .views import RegisterAPI, MyProfileAPI

urlpatterns = [
    path('register/', RegisterAPI.as_view()),
    path('my-profile/', MyProfileAPI.as_view())
]
