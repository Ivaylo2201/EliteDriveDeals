from django.db.models import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .models import Car
from .forms import CarForm

# Create your views here.

def home(request) -> HttpResponse:
    newest_car: Car = Car.objects.order_by('-posted_on')[0]

    return render(
        request=request,
        template_name='home.html',
        context={'car': newest_car}
    )

def fetch_new_cars(request) -> HttpResponse:
    cars: QuerySet = (
        Car.objects
            .filter(mileage=0)
            .order_by('id')
    )

    return render(
        request=request,
        template_name='cars.html',
        context={'cars': cars}
    )

def fetch_used_cars(request) -> HttpResponse:
    cars: QuerySet = (
        Car.objects
            .filter(mileage__gt=0)
            .order_by('id')
    )

    return render(
        request=request,
        template_name='cars.html',
        context={'cars': cars}
    )


def car_details(request, id: int) -> HttpResponse:
    car: Car = get_object_or_404(Car, id=id)

    car.views += 1
    car.save()

    return render(
        request=request,
        template_name='car-details.html',
        context={'car': car}
    )

def add_listing(request) -> HttpResponse | HttpResponseRedirect:
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='home')
    else:
        form = CarForm()

    return render(
        request=request,
        template_name='add-listing.html',
        context={'form': form}
    )

def edit_listing(request, id: int) -> HttpResponse | HttpResponseRedirect:
    car = Car.objects.get(id=id)

    if request.method == 'GET':
        car_data = {
            'brand': car.brand, 'model': car.model, 'image': car.image,
            'manufacture_year': car.manufacture_year, 'transmission': car.transmission,
            'horsepower': car.horsepower, 'mileage': car.mileage, 'price': car.price,
            'dealer': car.dealer
        }

        return render(
            request=request,
            template_name='edit-listing.html',
            context={
                'form': CarForm(initial=car_data),
                'car': car
            }
        )
    else:
        form = CarForm(request.POST)

        if form.is_valid():
            car.brand = form.cleaned_data['brand']
            car.model = form.cleaned_data['model']
            car.image = form.cleaned_data['image']
            car.manufacture_year = form.cleaned_data['manufacture_year']
            car.transmission = form.cleaned_data['transmission']
            car.horsepower = form.cleaned_data['horsepower']
            car.mileage = form.cleaned_data['mileage']
            car.price = form.cleaned_data['price']
            car.dealer = form.cleaned_data['dealer']

            car.save()

        return redirect(to='home')
