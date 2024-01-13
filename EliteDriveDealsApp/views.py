from django.db.models import QuerySet, Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import Car
from .forms import CarForm, DealerForm

# Create your views here.

def home(request) -> HttpResponse:
    car: Car = (
        Car.objects
            .filter(is_available=True)
            .order_by('-posted_on')
            .first()
    )

    return render(
        request=request,
        template_name='home.html',
        context={'car': car}
    )

def fetch_new_cars(request) -> HttpResponse:
    criteria = Q(is_available=True) & Q(mileage=0)

    cars: QuerySet = (
        Car.objects
            .filter(criteria)
            .order_by('id')
    )

    return render(
        request=request,
        template_name='cars.html',
        context={'cars': cars}
    )

def fetch_used_cars(request) -> HttpResponse:
    criteria = Q(is_available=True) & Q(mileage__gt=0)

    cars: QuerySet = (
        Car.objects
            .filter(criteria)
            .order_by('id')
    )

    return render(
        request=request,
        template_name='cars.html',
        context={'cars': cars}
    )


def car_details(request, id: int) -> HttpResponse:
    car: Car = Car.objects.get(id=id)

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
    car: Car = Car.objects.get(id=id)

    if request.method == 'GET':
        car_data = {k: v for k, v in car.__dict__.items()}
        car_data['dealer'] = car.dealer

        form = CarForm(initial=car_data)

        return render(
            request=request,
            template_name='edit-listing.html',
            context={'form': form, 'car': car}
        )
    else:
        form = CarForm(request.POST)

        if form.is_valid():
            for field, value in form.cleaned_data.items():
                setattr(car, field, value)

            car.save()

        return redirect(to='home')

def purchase_car(request, id: int) -> HttpResponseRedirect:
    car: Car = Car.objects.get(id=id)

    car.is_available = False
    car.save()

    return redirect(to='home')

def register_dealer(request) -> HttpResponse | HttpResponseRedirect:
    if request.method == 'POST':
        form = DealerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='home')
    else:
        form = DealerForm()

    return render(
        request=request,
        template_name='register-dealer.html',
        context={'form': form}
    )
