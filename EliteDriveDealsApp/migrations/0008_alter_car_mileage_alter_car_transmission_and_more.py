# Generated by Django 5.0 on 2024-01-04 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EliteDriveDealsApp', '0007_alter_car_dealer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='mileage',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(choices=[('', 'Transmission'), ('M', 'Manual'), ('A', 'Automatic')]),
        ),
        migrations.AlterField(
            model_name='dealer',
            name='city',
            field=models.CharField(choices=[('', 'Location'), ('S', 'Sofia'), ('P', 'Plovdiv'), ('V', 'Varna'), ('B', 'Burgas'), ('R', 'Ruse'), ('ST', 'Stara Zagora'), ('VT', 'Veliko Tarnovo'), ('SL', 'Sliven')]),
        ),
    ]
