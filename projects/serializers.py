from rest_framework import serializers

from projects.models import Project
from users.serializers import CustomUserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)
    id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "status",
            "created_by",
        )
        depth = 1
