# Generated by Django 5.0.6 on 2024-05-30 19:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightApp', '0003_alter_flight_departurecity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flightApp.passenger'),
        ),
    ]
