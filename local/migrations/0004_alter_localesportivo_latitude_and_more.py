# Generated by Django 5.1.3 on 2024-11-19 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0003_localesportivo_latitude_localesportivo_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localesportivo',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='localesportivo',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=12, null=True),
        ),
    ]
