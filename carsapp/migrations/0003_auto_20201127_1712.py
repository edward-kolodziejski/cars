# Generated by Django 3.1.3 on 2020-11-27 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carsapp', '0002_carrate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrate',
            name='rate_car_foreignkey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='carsapp.car'),
        ),
    ]
