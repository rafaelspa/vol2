# Generated by Django 4.0 on 2024-04-23 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_task_is_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='author',
            new_name='profile',
        ),
    ]
