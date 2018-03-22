from cars.models import CarModel
from django.shortcuts import render, get_object_or_404

def index(request):
    all_cars = CarModel.objects.all()
    return render(request, 'cars/index.html', {'all_cars': all_cars})


def detail(request, car_id):
    car = get_object_or_404(CarModel, id=car_id)
    return render(request, 'cars/detail.html', {'car': car})
