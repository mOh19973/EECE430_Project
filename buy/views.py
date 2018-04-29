from django.shortcuts import render, redirect
from cars.models import CarModel
from .models import BuyModel
from django.contrib.auth.models import User


def home(request, pk):
    buyCar = CarModel.objects.get(pk=pk)

    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        BuyModel.objects.create(boughtCar=buyCar.__str__(), buyer=user)
        CarModel.objects.get(pk=pk).delete()
        return redirect('cars:index')

    return render(request, 'buy/confirm_buy.html', {'pk': pk})
