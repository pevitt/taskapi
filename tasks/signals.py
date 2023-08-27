from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task


@receiver(post_save, sender=Task)
def task_post_save(sender, instance, **kwargs):
    print('task_post_save from tasks/signals.py')
    print('instance', instance.__dict__)
    print('kwargs', kwargs)
