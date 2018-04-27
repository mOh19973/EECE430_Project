from django.conf.urls import url
from . import views

app_name = 'testdrive'

urlpatterns = [
    # testdrive/booking/pk
    url(r'^booking/(?P<pk>[0-9]+)$', views.createTD, name='booking'),

    # testdrive/pk
    url(r'^details/(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),

    # /testdrive/pk/delete/
    url(r'^/(?P<pk>[0-9]+)/delete/$', views.TDDelete.as_view(), name='delete'),
]
