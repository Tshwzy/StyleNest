# Generated by Django 5.1.1 on 2024-09-20 16:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.service'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='sub_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.subservice'),
        ),
    ]
