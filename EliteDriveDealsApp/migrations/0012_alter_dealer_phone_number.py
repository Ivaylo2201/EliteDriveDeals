# Generated by Django 5.0 on 2024-01-04 20:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EliteDriveDealsApp', '0011_alter_car_brand_alter_car_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealer',
            name='phone_number',
            field=models.CharField(validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
