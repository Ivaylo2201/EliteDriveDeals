import datetime

from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator

from .choices import LOCATIONS, TRANSMISSIONS


class Dealer(models.Model):
    name = models.CharField(max_length=25)
    location = models.CharField(choices=LOCATIONS)
    phone_number = models.CharField(validators=[MinLengthValidator(10)])
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    brand = models.CharField(max_length=15)
    model = models.CharField(max_length=15)
    image = models.URLField(max_length=500)
    manufacture_year = models.PositiveSmallIntegerField(validators=[MaxValueValidator(datetime.date.today().year)])
    transmission = models.CharField(choices=TRANSMISSIONS)
    horsepower = models.PositiveSmallIntegerField()
    mileage = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    dealer = models.ForeignKey(to=Dealer, on_delete=models.CASCADE, related_name='listings')
    views = models.PositiveIntegerField(default=0)
    posted_on = models.DateField(auto_now_add=True)
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.brand} {self.model}'
