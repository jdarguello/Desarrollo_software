#Gestión de direcciones locales de la aplicación 'Usuarios'

from django.urls import path, include   #Creación de direcciones locales

from rest_framework.routers import DefaultRouter    #Gestión de direcciones de API's tipo ViewSet

from Usuarios.views import LoginAPI, LogoutAPI, PerfilAPI, UsuarioAPI

router = DefaultRouter()
router.register('usuarios', UsuarioAPI)
router.register('perfiles', PerfilAPI)

urlpatterns = [
    #Lista de direcciones
    path('crud/', include(router.urls)),
    path('logout', LogoutAPI.as_view()),
    path('login', LoginAPI.as_view())
]