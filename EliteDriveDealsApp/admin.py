from django.contrib import admin
from .models import Car, Dealer

# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [
        'brand', 'model', 'manufacture_year', 'transmission',
        'horsepower', 'mileage', 'price', 'dealer', 'views',
        'posted_on', 'is_available'
    ]

    list_filter = ['brand', 'manufacture_year', 'transmission', 'is_available']
    search_fields = ['brand', 'model']
    readonly_fields = ['views', 'posted_on', 'is_available']

@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'phone_number', 'date_joined']
    list_filter = ['location']
    search_fields = ['name', 'location']
    readonly_fields = ['date_joined']
