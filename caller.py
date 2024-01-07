import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EliteDriveDeals.settings")
django.setup()

from EliteDriveDealsApp.models import Car, Dealer

Dealer.objects.create(
    name='NitroGarage.org',
    location='Burgas',
    phone_number='0892350867'
)