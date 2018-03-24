
from django.conf.urls import url
from django.conf.urls.static import static

from EECE430_Project import settings
from . import views

app_name = 'cars'

urlpatterns = [
    # /Default landing page
    url(r'^$', views.index, name='index'),

    # /music/<car_id>/
    url(r'^(?P<car_id>[0-9]+)/$', views.detail,  name='search'),

]
