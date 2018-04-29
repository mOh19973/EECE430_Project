from django.conf.urls import url
from . import views

app_name = 'userphoto'

urlpatterns = [

    # /userphoto/username
    url(r'^(?P<username>[a-zA-Z0-9]+)$', views.addphoto, name='addphoto'),
]