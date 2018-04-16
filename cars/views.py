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
        carspecs =['CarBrand', 'Model', 'Year', 'Engine', 'Cylinders', 'DoorsNum',
                   'Weight', 'Fuel', 'BodyType', 'Transmission', 'HP', 'TopSpeed',
                   'FuelCapacity', 'Country', 'Mileage', 'Color']
        searchedItem = CarModel.objects.all()
        carList = CarModel.objects.all()
        form = self.form_class(request.GET)

        orderedByBrand = CarModel.objects.values('CarBrand').distinct().order_by('CarBrand').all()
        orderedByModel = CarModel.objects.values('Model').distinct().order_by('Model').all()
        orderedByYear = CarModel.objects.values('Year').distinct().order_by('Year').all()
        orderedByEngine = CarModel.objects.values('Engine').distinct().order_by('Engine').all()
        orderedByCylinders = CarModel.objects.values('Cylinders').distinct().order_by('Cylinders').all()
        orderedByDoors = CarModel.objects.values('DoorsNum').distinct().order_by('DoorsNum').all()
        orderedByWeight = CarModel.objects.values('Weight').distinct().order_by('Weight').all()
        orderedByFuel = CarModel.objects.values('Fuel').distinct().order_by('Fuel').all()
        orderedByBody = CarModel.objects.values('BodyType').distinct().order_by('BodyType').all()
        orderedByTrans = CarModel.objects.values('Transmission').distinct().order_by('Transmission').all()
        orderedByHP = CarModel.objects.values('HP').distinct().order_by('HP').all()
        orderedBySpeed = CarModel.objects.values('TopSpeed').distinct().order_by('TopSpeed').all()
        orderedByCap = CarModel.objects.values('FuelCapacity').distinct().order_by('FuelCapacity').all()
        orderedByCountry = CarModel.objects.values('Country').distinct().order_by('Country').all()
        orderedByMile = CarModel.objects.values('Mileage').distinct().order_by('Mileage').all()
        orderedByColor = CarModel.objects.values('Color').distinct().order_by('Color').all()

        year = request.GET.get("Year")
        carBrand = request.GET.get("CarBrand")
        model = request.GET.get("Model")
        engine = request.GET.get("Engine")
        cylinders = request.GET.get("Cylinders")
        doors = request.GET.get("DoorsNum")
        weight = request.GET.get("Weight")
        fuel = request.GET.get("Fuel")
        bodytype = request.GET.get("BodyType")
        transmission = request.GET.get("Transmission")
        hp = request.GET.get("HP")
        speed = request.GET.get("TopSpeed")
        cap = request.GET.get("FuelCapacity")
        country = request.GET.get("Country")
        mile = request.GET.get("Mileage")
        color = request.GET.get("Color")
        x = 0
        if form.is_valid():
            for i in carspecs:
                if not request.GET.get(i) == "All":
                    x = x+1
            if x == 16:
                searchedItem = CarModel.objects.filter(CarBrand=carBrand, Model=model, Year=year, Engine=engine,
                                                       Cylinders=cylinders, DoorsNum=doors, Weight=weight,
                                                       Fuel=fuel, BodyType=bodytype, Transmission=transmission,
                                                       HP=hp, TopSpeed=speed, FuelCapacity=cap, Country=country,
                                                       Mileage=mile, Color=color)

        return render(request, self.template_name, {'form': form,
                                                    'carList': carList,
                                                    'orderedByYear': orderedByYear,
                                                    'orderedByBrand': orderedByBrand,
                                                    'orderedByModel': orderedByModel,
                                                    'orderedByEngine': orderedByEngine,
                                                    'orderedByCylinders': orderedByCylinders,
                                                    'orderedByDoors': orderedByDoors,
                                                    'orderedByWeight': orderedByWeight,
                                                    'orderedByFuel': orderedByFuel,
                                                    'orderedByBody': orderedByBody,
                                                    'orderedByTrans': orderedByTrans,
                                                    'orderedByHP': orderedByHP,
                                                    'orderedBySpeed': orderedBySpeed,
                                                    'orderedByCountry': orderedByCountry,
                                                    'orderedByCap': orderedByCap,
                                                    'orderedByMile': orderedByMile,
                                                    'orderedByColor': orderedByColor,
                                                    'searchedItem': searchedItem})
