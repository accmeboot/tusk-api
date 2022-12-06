from rest_framework import serializers

from tasks.models import Task
from users.serializers import CustomUserSerializer


class TaskSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)
    assigned_to = CustomUserSerializer(read_only=True)
    id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "created_by",
            "assigned_to",
            "estimation",
            "project",
        )
