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
        exclude = ['CarImg']
        labels = {
            'CarBrand': 'Brand Name',
            'Model': 'Model Name',
            'DoorsNum': 'Number of Doors',
            'BodyType': 'Body Type',
            'HP': 'HorsePower',
            'TopSpeed': 'Top Speed',
            'FuelCapacity': 'Fuel Capacity'
        }
        CarModel.CarBrand = forms.ChoiceField(choices=[car for car in CarModel.objects.all()])

    def __init__(self, *args, **kwargs):
        super(CarModelForm, self).__init__(*args, **kwargs)
        self.fields['CarBrand'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Car Brand',
                                                     'id': 'username',
                                                     'style': 'margin-bottom: -1px; '
                                                              'border-bottom-right-radius: 0; '
                                                              'border-bottom-left-radius: 0; '
                                                              'border-top-left-radius: 0; '
                                                              'border-top-right-radius: 0;'})
        self.fields['Model'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username',
                                                     'id': 'username',
                                                     'style': 'margin-bottom: -1px; '
                                                              'border-bottom-right-radius: 0; '
                                                              'border-bottom-left-radius: 0; '
                                                              'border-top-left-radius: 0; '
                                                              'border-top-right-radius: 0;'})
        self.fields['BodyType'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username',
                                                     'id': 'username',
                                                     'style': 'margin-bottom: -1px; '
                                                              'border-bottom-right-radius: 0; '
                                                              'border-bottom-left-radius: 0; '
                                                              'border-top-left-radius: 0; '
                                                              'border-top-right-radius: 0;'})
        self.fields['HP'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username',
                                                     'id': 'username',
                                                     'style': 'margin-bottom: -1px; '
                                                              'border-bottom-right-radius: 0; '
                                                              'border-bottom-left-radius: 0; '
                                                              'border-top-left-radius: 0; '
                                                              'border-top-right-radius: 0;'})
        self.fields['TopSpeed'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username',
                                                     'id': 'username',
                                                     'style': 'margin-bottom: -1px; '
                                                              'border-bottom-right-radius: 0; '
                                                              'border-bottom-left-radius: 0; '
                                                              'border-top-left-radius: 0; '
                                                              'border-top-right-radius: 0;'})

        self.fields['FuelCapacity'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password',
                                                     'id': 'password'})
