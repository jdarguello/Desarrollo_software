from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter 

from .views import *

router = DefaultRouter()
router.register('users', UsuarioAPI)
router.register('perfil', PerfilAPI, basename="perfil")

urlpatterns = [
    path('crud/', include(router.urls))
]