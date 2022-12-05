from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    class Status(models.TextChoices):
        TODO = "TODO", _("To do")
        IN_PROGRESS = "IN_PROGRESS", _("In progress")
        DONE = "DONE", _("Done")

    name = models.CharField(max_length=512)
    created_by = models.ForeignKey(
        get_user_model(),
        null=True,
        on_delete=models.SET_NULL,
    )
    status = models.CharField(
        choices=Status.choices,
        default=Status.TODO,
        max_length=11,
    )

    def __str__(self) -> str:
        return self.name
