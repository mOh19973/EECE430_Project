from django.conf.urls import url
from . import views

app_name = 'cars'

urlpatterns = [
    # /Default landing page
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /cars/index/
    url(r'^index$', views.IndexView.as_view(), name='index'),

    # /cars/username
    url(r'^(?P<username>[a-zA-Z0-9]+)$', views.go_to_user, name='user_index'),

    # /cars/pk/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(),  name='detail'),

    # /cars/username/pk/
    url(r'^(?P<username>[a-zA-Z0-9]+)/(?P<pk>[0-9]+)/$', views.go_to_user_index,  name='user_detail'),

    # /cars/model/add
    url(r'^model/add/$', views.CarCreate.as_view(), name='cars-add'),

    # /cars/model/pk/
    url(r'^model/(?P<pk>[0-9]+)/$', views.CarUpdate.as_view(), name='cars-update'),

    # /cars/model/pk/delete/
    url(r'^model/(?P<pk>[0-9]+)/delete/$', views.CarDelete.as_view(), name='cars-delete'),
]
