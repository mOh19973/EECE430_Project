from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'cars/', include('cars.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
