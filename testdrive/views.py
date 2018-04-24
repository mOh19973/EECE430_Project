import datetime
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views import generic

from cars.models import CarModel
from .forms import TDForm
from django.contrib.auth.models import User
from .models import TDModel


class DetailView(generic.DetailView):
    template_name = 'testdrive/detail.html'
    model = TDModel
    context_object_name = 'testdrive'


def createTD(request, pk):
    upcoming = []
    testCar = CarModel.objects.get(pk=pk)
    carTestDrives = TDModel.objects.filter(driveCar=testCar)
    for drive in carTestDrives:
        if drive.driveDate > timezone.now():
            upcoming.append(drive)
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        car = CarModel.objects.get(id=pk)
        drive = request.POST['driveDate']
        if datetime.datetime.strptime(drive, '%Y-%m-%dT%H:%M') >= datetime.datetime.now() + datetime.timedelta(days=3):
            try:
                TDModel.objects.get(driveCar=car, driveDate=drive)
                return render(request, 'testdrive/fail.html', {'pk': pk})
            except ObjectDoesNotExist:
                    TDModel.objects.create(driveDate=drive, driveCar=car, driver=user)
                    return render(request, 'testdrive/success.html', {'pk': pk})
        else:
            return render(request, 'testdrive/pastTime.html', {'pk': pk})
    else:
        form = TDForm()
    return render(request, 'testdrive/createTD.html', {'form': form, 'pk': pk, 'upcoming': upcoming})
