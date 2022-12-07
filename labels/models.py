from django.db import models

from tasks.models import Task


class Label(models.Model):
    title = models.CharField(max_length=50)
    tasks = models.ManyToManyField(Task)

    def __str__(self):
        return self.title
