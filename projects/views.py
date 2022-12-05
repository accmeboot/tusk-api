from rest_framework import viewsets, permissions
from projects.models import Project

from projects.serializers import ProjectSerializer


class ProjectsViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [permissions.IsAuthenticated]
