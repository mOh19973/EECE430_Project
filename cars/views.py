from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import CarModel
from django.urls import reverse_lazy
from django.views import View
from django.views import generic
from .forms import CarModelForm


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
    fields = '__all__'


class CarUpdate(UpdateView):
    model = CarModel
    fields = '__all__'


class CarDelete(DeleteView):
    model = CarModel
    success_url = reverse_lazy('cars:index')


class Search(View):
    form_class = CarModelForm
    template_name = 'cars/SearchForm.html'

    # Display blank form
    def get(self, request):
        searchedItem = CarModel.objects.all()
        carList = CarModel.objects.all()
        form = self.form_class(request.GET)
        ordered = CarModel.objects.values('Year').distinct().order_by('Year').all()
        year = request.GET.get("Year")
        if form.is_valid():
            searchedItem = CarModel.objects.filter(Year=year)
        return render(request, self.template_name, {'form': form, 'carList': carList, 'ordered': ordered,
                                                    'searchedItem': searchedItem})
