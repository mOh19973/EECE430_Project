from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import CarModel
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'cars/index.html'
    context_object_name = 'carList'

    def get_queryset(self):
        return CarModel.objects.all()


class DetailView(generic.DetailView):
    context_object_name = 'car'
    model = CarModel
    template_name = 'cars/detail.html'


class CarCreate(CreateView):
    model = CarModel
    fields = ['CarImg', 'CarBrand', 'Model', 'Year', 'Engine','Cylinders','DoorsNum','Weight', 'Fuel', 'BodyType', 'Transmission',
              'HP', 'TopSpeed', 'FuelCapacity','Country', 'Mileage', 'Color']


class CarUpdate(UpdateView):
    model = CarModel
    fields = ['CarImg', 'CarBrand', 'Model', 'Year', 'Engine','Cylinders','DoorsNum','Weight', 'Fuel', 'BodyType', 'Transmission',
              'HP', 'TopSpeed', 'FuelCapacity','Country', 'Mileage', 'Color']


class CarDelete(DeleteView):
    model = CarModel
    success_url = reverse_lazy('cars:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'cars/registrationform.html'

    # Display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # Cleaned normalised data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns user objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('cars:index')

        return render(request, self.template_name, {'form': form})