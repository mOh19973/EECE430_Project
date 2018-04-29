from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
app_name = 'accounts'

urlpatterns = [

    # /accounts/register/
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /accounts/login
    url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),

    # /accounts/logout
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

    # /accounts/profile/
    url(r'^profile/(?P<username>[a-zA-Z0-9]+)$', views.get_user_profile, name='profile'),

    # /accounts/profile/username/edit
    url(r'^profile/(?P<username>[a-zA-Z0-9]+)/edit$', views.addphoto, name='addphoto'),

]