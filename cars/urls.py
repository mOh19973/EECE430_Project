from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'cars'

urlpatterns = [
    # /Default landing page
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^index$', views.IndexView.as_view(), name='index'),
    # /cars/pk/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(),  name='detail'),

    # /cars/model/add
    url(r'^model/add/$', views.CarCreate.as_view(), name='cars-add'),

    # /cars/model/pk/
    url(r'^model/(?P<pk>[0-9]+)/$', views.CarUpdate.as_view(), name='cars-update'),

    # /cars/model/pk/delete/
    url(r'^model/(?P<pk>[0-9]+)/delete/$', views.CarDelete.as_view(), name='cars-delete'),
]
