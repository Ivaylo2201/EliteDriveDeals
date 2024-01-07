import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EliteDriveDeals.settings")
django.setup()

from EliteDriveDealsApp.models import Car, Dealer

