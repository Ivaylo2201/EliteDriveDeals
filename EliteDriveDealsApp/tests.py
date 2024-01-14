from django.test import TestCase, Client
from django.urls import reverse

from .models import Car, Dealer
from datetime import date


# Create your tests here.

class CarTest(TestCase):
    def setUp(self):
        self.car = Car.objects.create(
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
        self.assertEqual(self.car.posted_on, date(2024, 1, 14))

    def test_car_is_available(self):
        self.assertEqual(self.car.is_available, True)

    def test_car_str_method(self):
        self.assertEqual(self.car.__str__(), 'test_brand test_model')


class DealerTest(TestCase):
    def setUp(self) -> None:
        self.dealer = Dealer.objects.create(
            name='test_name',
            location='Sofia',
            phone_number='0000000000'
        )

    def test_dealer_name(self) -> None:
        self.assertEqual(self.dealer.name, 'test_name')

    def test_dealer_location(self) -> None:
        self.assertEqual(self.dealer.location, 'Sofia')

    def test_dealer_phone_number(self) -> None:
        self.assertEqual(self.dealer.phone_number, '0000000000')

    def test_dealer_date_joined(self) -> None:
        self.assertEqual(self.dealer.date_joined, date(2024, 1, 14))

    def test_dealer_str_method(self) -> None:
        self.assertEqual(self.dealer.__str__(), 'test_name')


class ViewsTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.car = Car.objects.create(
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
        url = reverse('home')
        response = self.client.get(url)

        self.assertContains(response, 'Welcome To<br>EliteDriveDeals')
        self.assertContains(response, self.car.image)
        self.assertContains(response, 'Check out the latest listing!')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_new_cars_view(self) -> None:
        url = reverse('new-cars')
        response = self.client.get(url)

        attrs: list = [
            'car-card', self.car.image, self.car.transmission,
            self.car.horsepower, self.car.__str__(), 'Details'
        ]

        for a in attrs:
            self.assertContains(response, a)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cars.html')

    def test_used_cars_view(self) -> None:
        url = reverse('used-cars')
        response = self.client.get(url)

        # Since this and the above view use the same
        # template the previous test is enough for both views

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cars.html')

    def test_add_listing_view(self) -> None:
        url = reverse('add-listing')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 201)
        self.assertTemplateUsed(response, 'add-listing.html')

    def test_register_dealer_view(self) -> None:
        url = reverse('register-dealer')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 201)
        self.assertTemplateUsed(response, 'register-dealer.html')

    def test_car_details_view(self) -> None:
        url: str = '/car-details/1'
        response = self.client.get(url)

        fields: list = [
            'brand', 'model', 'manufacture_year', 'transmission',
            'horsepower', 'mileage', 'price', 'views',
        ]

        for f in fields:
            self.assertContains(response, getattr(self.car, f))

        self.assertContains(response, 'Jan. 14, 2024')
        self.assertContains(response, self.car.dealer.name)
        self.assertContains(response, self.car.dealer.location)
        self.assertContains(response, self.car.dealer.phone_number)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'car-details.html')

    def test_car_purchased_view(self) -> None:
        url: str = '/purchase-car/1'
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)  # Redirect -> No render template is used
        self.assertFalse(Car.objects.get(id=1).is_available)
