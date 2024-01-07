from django.urls import path
from EliteDriveDealsApp import views

urlpatterns = [
    #  path('', views.home),
    path('', views.home, name='home'),
    path('new-cars/', views.fetch_new_cars, name='new-cars'),
    path('used-cars/', views.fetch_used_cars, name='used-cars'),
    path('car-details/<int:id>', views.car_details, name='car-details'),
    path('add-listing/', views.add_listing, name='add-listing')
]