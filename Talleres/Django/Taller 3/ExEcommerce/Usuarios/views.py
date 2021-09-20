from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import authentication
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404

from Usuarios.serializers import *
from Usuarios.permissions import *

class UsuarioAPI(viewsets.ModelViewSet):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated, AccesoPerfil)
    serializer_class = UserSerial
    queryset = get_user_model().objects.all()


class PerfilAPI (viewsets.ModelViewSet):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated, AccesoPerfil)
    serializer_class = PerfilSerial
    queryset = Perfil.objects.all()



def login():
    pass

def logout():
    pass