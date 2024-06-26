# Generated by Django 5.0.6 on 2024-05-27 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsaApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='nsaApp.customer'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
