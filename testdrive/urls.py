from django.conf.urls import url
from .views import home, success
from . import views

app_name='testdrive'

urlpatterns = [
     url(r'^success/$', views.success, name='success'),
     url(r'^$', views.home, name='home'),
     url(r'^index$', views.IndexView.as_view(), name='index'),
     url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]