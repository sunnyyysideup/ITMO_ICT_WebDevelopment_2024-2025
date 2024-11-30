# Generated by Django 5.1.2 on 2024-11-25 19:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_administration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cleaningschedule',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cleaning_schedules', to='hotel_administration.client'),
        ),
    ]