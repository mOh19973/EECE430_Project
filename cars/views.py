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
        ordered = []
        for i in carspecs:
            ordered.append(CarModel.objects.values(i).distinct().order_by(i).all())

        form_data = []
        for l in carspecs:
            form_data.append(request.GET.get(l))

        x = 0
        if form.is_valid():
            for i in carspecs:
                if not request.GET.get(i) == "All":
                    x = x+1
            if x == 16:
                searchedItem = CarModel.objects.all().filter(CarBrand=form_data.__getitem__(0),
                                                             Model=form_data.__getitem__(1),
                                                             Year=form_data.__getitem__(2),
                                                             Engine=form_data.__getitem__(3),
                                                             Cylinders=form_data.__getitem__(4),
                                                             DoorsNum=form_data.__getitem__(5),
                                                             Weight=form_data.__getitem__(6),
                                                             Fuel=form_data.__getitem__(7),
                                                             BodyType=form_data.__getitem__(8),
                                                             Transmission=form_data.__getitem__(9),
                                                             HP=form_data.__getitem__(10),
                                                             TopSpeed=form_data.__getitem__(11),
                                                             FuelCapacity=form_data.__getitem__(12),
                                                             Country=form_data.__getitem__(13),
                                                             Mileage=form_data.__getitem__(14),
                                                             Color=form_data.__getitem__(15))

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
