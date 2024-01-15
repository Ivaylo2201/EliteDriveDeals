from django.http import HttpResponse
from django.test import TestCase, Client
from django.urls import reverse

from .models import Car, Dealer
from datetime import date
from typing import Any


# Create your tests here.

class CarTest(TestCase):
    def setUp(self):
        self.car: Car = Car.objects.create(
            brand='test_brand',
            model='test_model',
            image='test_image',
            manufacture_year=2024,
            transmission='Automatic',
            horsepower=100,
            mileage=0,
            price=10000,
            dealer=Dealer.objects.create(name='test_name', location='Sofia', phone_number='0000000000'),
        )


    def test_car_brand(self):
        self.assertEqual(self.car.brand, 'test_brand')


    def test_car_model(self):
        self.assertEqual(self.car.model, 'test_model')


    def test_car_image(self):
        self.assertEqual(self.car.image, 'test_image')


    def test_car_manufacture_year(self):
        self.assertEqual(self.car.manufacture_year, 2024)


    def test_car_transmission(self):
        self.assertEqual(self.car.transmission, 'Automatic')


    def test_car_horsepower(self):
        self.assertEqual(self.car.horsepower, 100)


    def test_car_mileage(self):
        self.assertEqual(self.car.mileage, 0)


    def test_car_price(self):
        self.assertEqual(self.car.price, 10000)


    def test_car_dealer(self):
        self.assertEqual(self.car.dealer.name, 'test_name')


    def test_car_views_default_value(self):
        self.assertEqual(self.car.views, 0)


    def test_car_posted_on(self):
        self.assertEqual(self.car.posted_on, date.today())


    def test_car_is_available(self):
        self.assertEqual(self.car.is_available, True)


    def test_car_str_method(self):
        self.assertEqual(self.car.__str__(), 'test_brand test_model')


class DealerTest(TestCase):
    def setUp(self) -> None:
<<<<<<< HEAD
        self.dealer: Dealer = Dealer.objects.create(name='test_name', location='Sofia', phone_number='0000000000')
=======
        self.dealer = Dealer.objects.create(
            name='test_name',
            location='Sofia',
            phone_number='0000000000',
        )
>>>>>>> c2dff65c4dce5b16543fa2b5d4c06376b2251cb6


    def test_dealer_name(self) -> None:
        self.assertEqual(self.dealer.name, 'test_name')


    def test_dealer_location(self) -> None:
        self.assertEqual(self.dealer.location, 'Sofia')


    def test_dealer_phone_number(self) -> None:
        self.assertEqual(self.dealer.phone_number, '0000000000')


    def test_dealer_date_joined(self) -> None:
        self.assertEqual(self.dealer.date_joined, date.today())


    def test_dealer_str_method(self) -> None:
        self.assertEqual(self.dealer.__str__(), 'test_name')


class ViewsTest(TestCase):
    def setUp(self) -> None:
        self.client: Client = Client()
        self.car: Car = Car.objects.create(
            id=1,
            brand='test_brand',
            model='test_model',
            image='test_image',
            manufacture_year=2024,
            transmission='Automatic',
            horsepower=100,
            mileage=0,
            price=10000,
            dealer=Dealer.objects.create(name='test_name', location='Sofia', phone_number='0000000000'),
        )


    def test_home_view(self) -> None:
        url: str = reverse('home')
        response: HttpResponse = self.client.get(url)

        self.assertContains(response, 'Welcome To<br>EliteDriveDeals')
        self.assertContains(response, self.car.image)
        self.assertContains(response, 'Check out the latest listing!')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


    def test_new_cars_view(self) -> None:
        url: str = reverse('new-cars')
        response: HttpResponse = self.client.get(url)

        attrs: list[str] = [
            'car-card', self.car.image, self.car.transmission,
            self.car.horsepower, self.car.__str__(), 'Details'
        ]

        for a in attrs:
            self.assertContains(response, a)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cars.html')


    def test_used_cars_view(self) -> None:
        url: str = reverse('used-cars')
        response: HttpResponse = self.client.get(url)

        # Since this and the above view use the same
        # template the previous test is enough for both views

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cars.html')


    def test_add_listing_view_get(self) -> None:
        url: str = reverse('add-listing')
        response: HttpResponse = self.client.get(url)

        self.assertEqual(response.status_code, 201)
        self.assertTemplateUsed(response, 'add-listing.html')


    def test_add_listing_view_post(self) -> None:
        url: str = reverse('add-listing')
        data: dict[str, Any] = {
            'brand': 'test_brand', 'model': 'test_model',
            'image': 'https://content.api.news/v3/images/bin/bad661b374f7730fbbd29dc9b2f6ea3f',
            'manufacture_year': 2015, 'transmission': 'Automatic',
            'horsepower': 150, 'mileage': 200000, 'price': 20000,
            'dealer': self.car.dealer
        }
        response: HttpResponse = self.client.post(url, data=data)

        is_added: bool = (
            Car.objects
            .filter(brand='test_brand', model='test_model')
            .exists()
        )

        self.assertTrue(is_added)
        self.assertEqual(response.status_code, 201)


    def test_register_dealer_view_get(self) -> None:
        url: str = reverse('register-dealer')
        response: HttpResponse = self.client.get(url)

        self.assertEqual(response.status_code, 201)
        self.assertTemplateUsed(response, 'register-dealer.html')


    def test_register_dealer_view_post(self) -> None:
        url: str = reverse('register-dealer')
        data: dict[str, str] = {'name': 'test_name', 'location': 'Varna', 'phone_number': '0000000000'}
        response: HttpResponse = self.client.post(url, data)

        is_registered: bool = (
            Dealer.objects
            .filter(name='test_name', location='Varna', phone_number='0000000000')
            .exists()
        )

        self.assertTrue(is_registered)
        self.assertEqual(response.status_code, 302)


    def test_car_details_view(self) -> None:
        url: str = '/car-details/1'
        response: HttpResponse = self.client.get(url)

        fields: list[str] = [
            'brand', 'model', 'manufacture_year', 'transmission',
            'horsepower', 'mileage', 'price', 'views',
        ]

        for f in fields:
            self.assertContains(response, getattr(self.car, f))

        # Converting to Django date format
        self.assertContains(response, date.today().strftime('%b. %d, %Y'))
        self.assertContains(response, self.car.dealer.name)
        self.assertContains(response, self.car.dealer.location)
        self.assertContains(response, self.car.dealer.phone_number)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'car-details.html')


    def test_car_purchased_view(self) -> None:
        url: str = '/purchase-car/1'
        response: HttpResponse = self.client.get(url)

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Car.objects.get(id=1).is_available)
