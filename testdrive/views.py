from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from .forms import TDForm
from .models import TDModel


class IndexView(generic.ListView):
    template_name = 'testdrive/index.html'
    context_object_name = 'testdriveList'

    def get_queryset(self):
        return TDModel.objects.all()


class DetailView(generic.DetailView):
    template_name='testdrive/detail.html'
    context_object_name = 'testdriveList'
    form = TDForm


def home(request):
    if request.method == 'POST':
        form = TDForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            username = formdata['username']
            carName = formdata['carName']
            day = formdata['day']
            month = formdata['month']
            year = formdata['year']
            hour = formdata['hour']
            minutes = formdata['minutes']
            TDModel.objects.create(username=username, carName=carName, day=day, month=month, year=year,
                                     hour=hour, minutes=minutes)
            return HttpResponseRedirect('/testdrive/success')        #redirected to success page
    else:
        form = TDForm()
    return render(request, 'testdrive/createTD.html', {'form': form})


def success(request):
    return render(request, 'testdrive/success.html')