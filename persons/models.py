from django.db import models
from django.contrib.auth.models import User

from utils.models import BaseModelUUID

# Create your models here.
class Person(BaseModelUUID):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        related_name='person'
    )
    first_name = models.CharField(
        max_length=100
    )
    last_name = models.CharField(
        max_length=100
    )
    email = models.EmailField(
        max_length=100, 
        unique=True
    )
    address = models.CharField(
        max_length=200
    )
    city = models.CharField(
        max_length=100
    )
    country = models.CharField(
        max_length=100
    )

    class Meta:
        db_table = 'persons'
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'
        ordering = ['created_at']
        indexes = [
            models.Index(
                fields=['email'], 
                name='email_idx'
            ),
        ]
    
    def __str__(self):
        return f'{self.email}'
    
