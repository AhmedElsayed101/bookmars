# Generated by Django 3.0.14 on 2022-02-16 14:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Actions',
            new_name='Action',
        ),
    ]
