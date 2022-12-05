from rest_framework import generics, status
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.response import Response

from .serializers import CustomUserSignupSerializer


class CustomUserSignupView(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = CustomUserSignupSerializer
    permission_classes = [
        permissions.AllowAny,
    ]

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)

        return Response(status=status.HTTP_201_CREATED)
