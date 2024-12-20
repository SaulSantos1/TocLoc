# Generated by Django 5.1.3 on 2024-11-19 16:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('disponibilidade', '0001_initial'),
        ('local', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disponibilidade',
            name='local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disponibilidades', to='local.localesportivo'),
        ),
        migrations.AlterUniqueTogether(
            name='disponibilidade',
            unique_together={('local', 'data', 'horario_inicio', 'horario_fim')},
        ),
    ]
