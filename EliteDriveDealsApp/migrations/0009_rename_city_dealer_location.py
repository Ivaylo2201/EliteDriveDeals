# Generated by Django 5.0 on 2024-01-04 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EliteDriveDealsApp', '0008_alter_car_mileage_alter_car_transmission_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dealer',
            old_name='city',
            new_name='location',
        ),
    ]
