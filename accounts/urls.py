from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
app_name = 'accounts'

urlpatterns = [
    # /accounts/
    # url(r'^$', views.IndexView.as_view(), name='default'),

    # /accounts/register/
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /accounts/login
    url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),

    # /accounts/logout
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

    # /accounts/profile/
    # url(r'^profile/$', views.AdminIndexView.as_view(), name='profile'),

]