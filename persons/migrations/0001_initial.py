# Generated by Django 4.2.3 on 2023-07-20 21:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='person', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
                'db_table': 'persons',
                'ordering': ['created_at'],
                'indexes': [models.Index(fields=['email'], name='email_idx')],
            },
        ),
    ]