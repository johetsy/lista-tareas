# Generated by Django 3.2.13 on 2023-08-04 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrar', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarea',
            old_name='tittle',
            new_name='title',
        ),
    ]
