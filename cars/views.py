from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import CarModel
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'cars/index.html'
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


def go_to_user(request, username):
    user = User.objects.get(username=username)
    carList = CarModel.objects.all()
    return render(request, 'cars/admin_index.html', {"user": user, "carList": carList})
