from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from testdrive.models import TDModel
from .forms import UserForm
from buy.models import BuyModel


def get_user_profile(request, username):
    user = User.objects.get(username=username)
    upcoming = []
    boughtCars = []
    testdrive = TDModel.objects.filter(driver=user)
    bought = BuyModel.objects.filter(buyer=user)
    for drive in testdrive:
        if drive.driveDate> timezone.now():
            upcoming.append(drive)
    for car in bought:
        boughtCars.append(car)
    return render(request, 'accounts/user_profile.html', {"user": user, 'upcoming': upcoming, 'boughtCars': boughtCars})


class UserFormView(View):
    user = User
    form_class = UserForm
    template_name = 'accounts/RegistrationForm.html'

    # Display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)
        isnotReg = False
        if form.is_valid():
            user = form.save(commit=False)

            # Cleaned normalised data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.set_password(password)
            user.save()

            # returns user objects if credentials are correct
            user = authenticate(username=username, password=password)


            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('accounts:profile', username)

        isnotReg = True
        return render(request, self.template_name, {'form': form, 'isnotReg': isnotReg})


