# Generated by Django 5.1.1 on 2024-10-02 08:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=255)),
                ('review_text', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='reviews/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('rating', models.PositiveIntegerField(default=5)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]