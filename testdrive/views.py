from django.shortcuts import render
from django.views import generic

from cars.models import CarModel
from .forms import TDForm
from django.contrib.auth.models import User
from .models import TDModel


class IndexView(generic.ListView):
    template_name = 'testdrive/index.html'
    context_object_name = 'testdrive'

    def get_queryset(self):
        return TDModel.objects.all()


class DetailView(generic.DetailView):
    template_name = 'testdrive/detail.html'
    context_object_name = 'testdriveList'
    form = TDForm


def home(request, pk):

    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        car = CarModel.objects.get(id=pk)
        drive = request.POST['driveDate']
        TDModel.objects.create(driveDate=drive, driveCar=car, driver=user)
        return render(request, 'testdrive/success.html')
    else:
        form = TDForm()
    return render(request, 'testdrive/createTD.html', {'form': form})


def success(request):
    return render(request, 'testdrive/success.html')
