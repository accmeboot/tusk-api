from rest_framework import permissions, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TasksViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("project",)
