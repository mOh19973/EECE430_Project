
from django.conf.urls import url
from django.conf.urls.static import static

from EECE430_Project import settings
from . import views

app_name = 'cars'

urlpatterns = [
    # /Default landing page
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),

    # /Car details/
    url(r'^(?P<car_id>[0-9]+)/$', views.detail,  name='detail'),

    #Admin Login page
    url(r'^login', views.login, name='admin_login'),

    #User Login page
    url(r'^user_login', views.user_login, name='user_login'),

    #admin area
    url(r'^administrator', views.administrator, name='login'),

    #user area
    # url(r'^login', views.login, name='login'),

    #logout
    url(r'^logout', views.logout, name='logout'),
]
