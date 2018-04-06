from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import CarModel
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import generic, View
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'cars/default_index.html'
    context_object_name = 'carList'

    def get_queryset(self):
        return CarModel.objects.all()


class DetailView(generic.DetailView):
    context_object_name = 'car'
    model = CarModel
    template_name = 'cars/detail.html'


class CarCreate(CreateView):
    model = CarModel
    fields = ['CarImg', 'CarBrand', 'Model', 'Year', 'Engine','Cylinders','DoorsNum','Weight', 'Fuel', 'BodyType', 'Transmission',
              'HP', 'TopSpeed', 'FuelCapacity','Country', 'Mileage', 'Color']


class CarUpdate(UpdateView):
    model = CarModel
    fields = ['CarImg', 'CarBrand', 'Model', 'Year', 'Engine','Cylinders','DoorsNum','Weight', 'Fuel', 'BodyType', 'Transmission',
              'HP', 'TopSpeed', 'FuelCapacity','Country', 'Mileage', 'Color']


class CarDelete(DeleteView):
    model = CarModel
    success_url = reverse_lazy('cars:index')


