from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rutas/api/', include('Rutas.urls')),
    path('aerolineas/api/', include('Aerolineas.urls')),
    path('usuarios/api/', include('Usuarios.urls'))
]
