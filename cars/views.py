from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView
from .models import CarModel
from django.urls import reverse_lazy
from django.views import View
from django.views import generic
from .forms import CarModelForm
from buy.models import BuyModel
import datetime


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
    buyer = BuyModel


def CarCreate(request):
    user = User.objects.get(username=request.user)
    form = CarModelForm
    if request.method == 'POST':
        carspecs = ['CarBrand',
                    'Model',
                    'Year',
                    'Engine',
                    'GearNum',
                    'TransmissionType',
                    'DoorsNum',
                    'Weight',
                    'Fuel',
                    'BodyType',
                    'CylindersNum',
                    'CylindersType',
                    'HP',
                    'TopSpeed',
                    'FuelCapacity',
                    'Country',
                    'Mileage',
                    'Color']

        form_data = []
        for l in carspecs:
            form_data.append(request.POST.get(l))

        carBrand = form_data.__getitem__(0).capitalize()
        model = form_data.__getitem__(1).capitalize()
        year=datetime.datetime.strptime(form_data.__getitem__(2), '%Y-%m').year.__str__() + '-01-01'
        engine = form_data.__getitem__(3)
        transmission = form_data.__getitem__(4) + ' SP '+ form_data.__getitem__(5)
        doorsNum = form_data.__getitem__(6)
        weight = form_data.__getitem__(7)
        fuelType = form_data.__getitem__(8)
        bodyType = form_data.__getitem__(9)
        cylinders = form_data.__getitem__(11) + ' ' + form_data.__getitem__(10)
        hp = form_data.__getitem__(12)
        topSpeed = form_data.__getitem__(13)
        fuelCap = form_data.__getitem__(14)
        country = form_data.__getitem__(15)
        mileage = form_data.__getitem__(16)
        color = form_data.__getitem__(17).capitalize()

        CarModel.objects.create(CarBrand=carBrand,
                                Model=model,
                                Year=year,
                                Engine=engine,
                                Transmission=transmission,
                                DoorsNum=doorsNum,
                                Weight=weight,
                                Fuel=fuelType,
                                BodyType=bodyType,
                                Cylinders=cylinders,
                                HP=hp,
                                TopSpeed=topSpeed,
                                FuelCapacity=fuelCap,
                                Country=country,
                                Mileage=mileage,
                                Color=color)
        return redirect('cars:index')

    return render(request, 'cars/CarModel_add.html', {'user': user, 'form':form})


class CarUpdate(UpdateView):
    model = CarModel
    form_class = CarModelForm
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

        if not form_data[0] == "All":
            searchedItem = searchedItem.filter(CarBrand=form_data.__getitem__(0))
        if not form_data[1] == "All":
            searchedItem = searchedItem.filter(Model=form_data.__getitem__(1))
        if not form_data[2] == "All" and not form_data[2] is None:
            year = datetime.datetime(datetime.datetime.strptime(form_data.__getitem__(2), '%Y').year, 1, 1)
            searchedItem = searchedItem.filter(Year=year)
        else:
            searchedItem = searchedItem.all()
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
