# Generated by Django 5.1.1 on 2024-09-20 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_alter_booking_service_alter_booking_sub_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='service',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='booking',
            name='sub_service',
            field=models.CharField(max_length=255),
        ),
    ]
