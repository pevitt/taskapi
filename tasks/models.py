from django.db import models
from utils.models import BaseModel, BaseModelUUID
from persons.models import Person


# Create your models here.
class TaskStatus(BaseModel):
    name = models.CharField(
        max_length=100
    )
    description = models.TextField(
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'task_status'
        verbose_name = 'Task Status'
        verbose_name_plural = 'Task Statuses'
        ordering = ['created_at']

    def __str__(self):
        return f'{self.name}'


class Task(BaseModelUUID):
    person = models.ForeignKey(
        'persons.Person',
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    title = models.CharField(
        max_length=100
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    status = models.ForeignKey(
        'tasks.TaskStatus',
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    order = models.IntegerField(
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        indexes = [
            models.Index(
                fields=['title'],
                name='title_idx'
            )
        ]

    def __str__(self):
        return f'{self.title}'
