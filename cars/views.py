from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import CarModel
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'cars/index.html'
    context_object_name = 'carList'
    user = User

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


def search(request):
        # Your code
        if request.method == 'GET':  # If the form is submitted

            search_query = request.GET.get('search_box', None)
            # Do whatever you need with the word the user looked for

        # Your code




