from django import forms
from django.forms import ModelForm
from .models import Car


class CarForm(ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super(CarForm, self).__init__(*args, **kwargs)
        self.fields['dealer'].empty_label = 'Dealer'

    class Meta:
        model = Car
        fields = [
            'brand', 'model', 'image',
            'manufacture_year', 'transmission',
            'horsepower', 'mileage', 'price', 'dealer'
        ]

        widgets = {
            'brand': forms.TextInput(attrs={'placeholder': 'Brand'}),
            'model': forms.TextInput(attrs={'placeholder': 'Model'}),
            'image': forms.TextInput(attrs={'placeholder': 'Image URL'}),
            'manufacture_year': forms.NumberInput(attrs={'placeholder': 'Manufacture year'}),
            'horsepower': forms.NumberInput(attrs={'placeholder': 'Horsepower'}),
            'mileage': forms.NumberInput(attrs={'placeholder': 'Mileage'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price'}),
        }
