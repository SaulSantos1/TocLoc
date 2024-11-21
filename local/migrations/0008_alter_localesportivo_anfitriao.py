# Generated by Django 5.1.3 on 2024-11-20 21:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0007_alter_localesportivo_nome'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='localesportivo',
            name='anfitriao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locais', to=settings.AUTH_USER_MODEL),
        ),
    ]
