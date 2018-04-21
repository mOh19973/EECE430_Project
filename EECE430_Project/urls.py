from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^$', views.homepage, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^cars/', include('cars.urls'), name='car'),
    url(r'^accounts/', include('accounts.urls'), name='accounts'),
    url(r'^testdrive/', include('testdrive.urls'), name='testdrive'),
    url(r'^account/$', views.account_redirect, name='account-redirect'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
