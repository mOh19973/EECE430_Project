from django.http import HttpResponse
from cars.models import CarModel
from django.shortcuts import render
from django.http import Http404

def index(request):
    all_cars = CarModel.objects.all()
    return render(request, 'cars/index.html', {'all_cars': all_cars})


def detail(request, car_id):
    try:
        car = CarModel.objects.get(id=car_id)
    except CarModel.DoesNotExist:
        raise Http404("Car does not exist")
    return render(request, 'cars/detail.html', {'car': car})
