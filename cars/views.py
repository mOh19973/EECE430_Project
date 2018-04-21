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
    user = User


class CarCreate(CreateView):
    model = CarModel
    fields = '__all__'
    user = User


class CarUpdate(UpdateView):
    model = CarModel
    fields = '__all__'
    user = User


class CarDelete(DeleteView):
    model = CarModel
    success_url = reverse_lazy('cars:index')
    user = User


class Search(View):
    form_class = CarModelForm
    user = User
    template_name = 'cars/SearchForm.html'

    def get(self, request):
        carspecs = ['CarBrand', 'Model', 'Year', 'Engine', 'Cylinders', 'DoorsNum',
                    'Weight', 'Fuel', 'BodyType', 'Transmission', 'HP', 'TopSpeed',
                    'FuelCapacity', 'Country', 'Mileage', 'Color']

        searchedItem = CarModel.objects.all()
        carList = CarModel.objects.all()
        form = self.form_class(request.GET)

        ordered = []
        for i in carspecs:
            ordered.append(CarModel.objects.values(i).distinct().order_by(i).all())

        form_data = []
        for l in carspecs:
            form_data.append(request.GET.get(l))

        if form.is_valid():
            if not form_data[0] == "All":
                searchedItem = searchedItem.filter(CarBrand=form_data.__getitem__(0))
            if not form_data[1] == "All":
                searchedItem = searchedItem.filter(Model=form_data.__getitem__(1))
            if not form_data[2] == "All":
                searchedItem = searchedItem.filter(Year=form_data.__getitem__(2))
            if not form_data[3] == "All":
                searchedItem = searchedItem.filter(Engine=form_data.__getitem__(3))
            if not form_data[4] == "All":
                searchedItem = searchedItem.filter(Cylinders=form_data.__getitem__(4))
            if not form_data[5] == "All":
                searchedItem = searchedItem.filter(DoorsNum=form_data.__getitem__(5))
            if not form_data[6] == "All":
                searchedItem = searchedItem.filter(Weight=form_data.__getitem__(6))
            if not form_data[7] == "All":
                searchedItem = searchedItem.filter(Fuel=form_data.__getitem__(7))
            if not form_data[8] == "All":
                searchedItem = searchedItem.filter(BodyType=form_data.__getitem__(8))
            if not form_data[9] == "All":
                searchedItem = searchedItem.filter(Transmission=form_data.__getitem__(9))
            if not form_data[10] == "All":
                searchedItem = searchedItem.filter(HP=form_data.__getitem__(10))
            if not form_data[11] == "All":
                searchedItem = searchedItem.filter(TopSpeed=form_data.__getitem__(11))
            if not form_data[12] == "All":
                searchedItem = searchedItem.filter(FuelCapacity=form_data.__getitem__(12))
            if not form_data[13] == "All":
                searchedItem = searchedItem.filter(Country=form_data.__getitem__(13))
            if not form_data[14] == "All":
                searchedItem = searchedItem.filter(Mileage=form_data.__getitem__(14))
            if not form_data[15] == "All":
                searchedItem = searchedItem.filter(Color=form_data.__getitem__(15))

        template_dict = \
            {
                'form': form,
                'carList': carList,
                'orderedByBrand': ordered[0],
                'orderedByModel': ordered[1],
                'orderedByYear': ordered[2],
                'orderedByEngine': ordered[3],
                'orderedByCylinders': ordered[4],
                'orderedByDoors': ordered[5],
                'orderedByWeight': ordered[6],
                'orderedByFuel': ordered[7],
                'orderedByBody': ordered[8],
                'orderedByTrans': ordered[9],
                'orderedByHP': ordered[10],
                'orderedBySpeed': ordered[11],
                'orderedByCap': ordered[12],
                'orderedByCountry': ordered[13],
                'orderedByMile': ordered[14],
                'orderedByColor': ordered[15],
                'searchedItem': searchedItem
            }
        return render(request, self.template_name, template_dict)
