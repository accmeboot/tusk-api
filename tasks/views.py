from rest_framework import permissions, viewsets
from tasks.models import Task

from tasks.serializers import TaskSerializer


class TasksViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [permissions.IsAuthenticated]
