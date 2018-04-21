from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic

from cars.models import CarModel
from .forms import TDForm
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
        form = TDForm(request.POST)
        if form.is_valid():
            user = request.user
            car = CarModel.objects.get(pk=pk)
            drive = form.cleaned_data['driveDate']

            TDModel.objects.create(driveDate=drive, driveCar=car, driver=user)
            return render(request, 'testdrive/success.html')
    else:
        form = TDForm()
    return render(request, 'testdrive/createTD.html', {'form': form})


def success(request):
    return render(request, 'testdrive/success.html')
