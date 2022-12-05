from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import CustomUser


class CustomUserSignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())],
    )
    password = serializers.CharField(
        required=True,
        write_only=True,
        validators=[
            validate_password,
        ],
        style={
            "input_type": "password",
        },
    )
    confirm_password = serializers.CharField(
        required=True,
        write_only=True,
        style={
            "input_type": "password",
        },
    )

    class Meta:
        model = CustomUser
        fields = (
            "email",
            "password",
            "confirm_password",
            "first_name",
            "last_name",
            "role",
        )

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {
                    "confirm_password": "Passwords must match",
                    "password": "Passwords must match",
                },
            )

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data["email"],
        )
        user.set_password(
            validated_data["password"],
        )
        user.save()

        return user
