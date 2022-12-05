from django.contrib.auth import get_user_model
from django.db import models

from projects.models import Project


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
    )
    assigned_to = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_user",
    )
    estimation = models.IntegerField()
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.title
