from django.shortcuts import render
from .models import CarModel
from .models import BuyModel
from django.contrib.auth.models import User

# Create your views here.
def home(request, pk):
    buyCar = CarModel.objects.get(pk = pk)

    if request.method == 'POST':
        user = User.objects.get(username = request.user)
        BuyModel.object.create(boughtCar = buyCar.__str__, buyer = user)
        CarModel.objects.get(pk=pk).delete()

    return render(request, 'buy/confirm_buy.html')