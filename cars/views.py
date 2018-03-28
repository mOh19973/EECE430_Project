from cars.models import *
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.hashers import *
from django.shortcuts import redirect

def index(request):
    all_cars = CarModel.objects.all()
    return render(request, 'cars/index.html', {'all_cars': all_cars})


def detail(request, car_id):
    car = get_object_or_404(CarModel, id=car_id)
    return render(request, 'cars/detail.html', {'car': car})

def login(request):
    # all_cars = CarModel.objects.all()
    if 'logged_in' in request.session:
        if 'admin' in request.session:
            if request.session['admin'] == 'true':
                return redirect('administrator.html')
        else:
                return render(request, 'cars/login.html')
    else:
        return render(request, 'cars/login.html')

def logout(request):
    request.session.clear()
    return redirect( request.META.get('HTTP_REFERER') )

# def admin_actions(request):


def user_login(request):
    if 'logged_in' in request.session:
        if request.session['customer'] == 'true':
            return redirect('index.html')
    else:

        if 'username' in request.POST and 'password' in request.POST:
            username = request.POST['username']
            pwd = make_password(request.POST['password'])

            try:
                result = Customer.objects.get(username__exact=username)
            except Customer.DoesNotExist:
                result = None

            if not result:
                message = 'Wrong Username/Password'
                return render(request, 'cars/user_login.html', {'error': message})
            else:
                password_check = check_password(request.POST['password'],result.password)
                if password_check == False:
                    message = 'Wrong Username/Password'
                    return render(request, 'cars/user_login.html', {'error': message})
                else:
                    request.session['logged_in'] = 'true'
                    request.session['customer'] = 'true'
                    request.session['customer_full_name'] = result.full_name
                    full_name = result.full_name
                    # full_name = request.session['fav_color']
                    return redirect('index.html')

        else:
            return render(request, 'cars/user_login.html')


def administrator(request):

#  THIS IS THE LOGIN FOR ADMINS
    if 'logged_in' in request.session:
        if request.session['admin'] == 'true':
            return render(request, 'cars/administrator.html', {'name': request.session['full_name']})
    else:

        if 'username' in request.POST and 'password' in request.POST:
            username = request.POST['username']
            pwd = make_password(request.POST['password'])

            try:
                result = Administrator.objects.get(username__exact=username)
            except Administrator.DoesNotExist:
                result = None

            if not result:
                message = 'Wrong Username/Password'
                return render(request, 'cars/login.html', {'error': message})
            else:
                password_check = check_password(request.POST['password'],result.password)
                if password_check == False:
                    message = 'Wrong Username/Password'
                    return render(request, 'cars/login.html', {'error': message})
                else:
                    request.session['logged_in'] = 'true'
                    request.session['admin'] = 'true'
                    request.session['full_name'] = result.full_name
                    full_name = result.full_name
                    # full_name = request.session['fav_color']
                    return render(request, 'cars/administrator.html', {'name': request.session['full_name']})

        else:
            message = "Please login"
            return redirect('login.html')
