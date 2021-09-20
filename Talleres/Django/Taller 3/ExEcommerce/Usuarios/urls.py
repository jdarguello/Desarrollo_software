from django.urls import path, include
from rest_framework.routers import DefaultRouter 

from Usuarios.views import *

router = DefaultRouter()
router.register('users', UsuarioAPI)
router.register('perfil', PerfilAPI)

urlpatterns = [
    path('crud/', include(router.urls)),
    path('register', RegisterAPI.as_view()),
    path('login', LoginAPI.as_view()),
    path('logout', LogoutAPI.as_view())
]