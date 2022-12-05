from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import CustomUserSignupView


urlpatterns = [
    path("signin/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("signup/", CustomUserSignupView.as_view()),
]
