# Generated by Django 5.0.6 on 2024-06-02 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightApp', '0004_alter_reservation_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='middletName',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
