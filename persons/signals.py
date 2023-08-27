from asgiref.sync import sync_to_async
from django.db.models.signals import post_save
from django.dispatch import receiver
from tasks.models import Task


@receiver(post_save, sender=Task)
@sync_to_async
def task_post_save(sender, instance, **kwargs):
    print('task_post_save from persons/signals.py')
    print('instance', instance.__dict__)
    print('kwargs', kwargs)

