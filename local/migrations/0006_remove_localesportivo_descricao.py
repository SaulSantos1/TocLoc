# Generated by Django 5.1.3 on 2024-11-19 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0005_alter_localesportivo_latitude_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localesportivo',
            name='descricao',
        ),
    ]
