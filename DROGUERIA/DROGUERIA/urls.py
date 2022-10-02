from django.contrib import admin
from django.urls import path, include
from App_DROGUERIA.views import Inicio 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Inicio, name = "Inicio"),
    path('App-Drogueria/', include("App_DROGUERIA.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
