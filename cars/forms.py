from django.contrib.auth.models import User
from django import forms

from cars.models import CarModel


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class CarModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'
        labels = {
            'CarBrand': 'Brand Name',
            'Model': 'Model Name',
            'DoorsNum': 'Number of Doors',
            'BodyType': 'Body Type',
            'HP': 'Horsepower',
            'TopSpeed': 'Top Speed',
            'FuelCapacity': 'Fuel Capacity',
            'Fuel': 'Fuel Type',
            'Engine': 'Engine Size'
        }
        CarModel.CarBrand = forms.ChoiceField(choices=[car for car in CarModel.objects.all()])

    def __init__(self, *args, **kwargs):
        super(CarModelForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
