# Generated by Django 5.1.3 on 2024-11-19 16:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('local', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='localesportivo',
            name='anfitriao',
            field=models.ForeignKey(limit_choices_to={'tipo_usuario': 'ANFITRIAO'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]