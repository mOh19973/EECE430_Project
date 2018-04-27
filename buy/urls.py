from django.conf.urls import url
from . import views

app_name = 'buy'

urlpatterns = [

    # /cars/buy/pk
    url(r'^(?P<pk>[0-9]+)$', views.home, name='home'),
]
