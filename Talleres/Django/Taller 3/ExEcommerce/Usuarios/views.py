from rest_framework.response import Response
from rest_framework import viewsets, views
from rest_framework import authentication
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.contrib.auth import authenticate, login, logout

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


class RegisterAPI(views.APIView):
    def post(self, request):
        usuario = UserSerial(data=request.data)
        if usuario.is_valid():
            #¿Información válida?
            usuario.save()
            return Response({"Bienvenido": False})
        return Response(usuario.errors, HTTP_400_BAD_REQUEST)

class LoginAPI(views.APIView):
    def post(self, request):
        usuario = authenticate(request, username=request.data['username'], password = request.data['password'])
        if not usuario is None:
            login(request, usuario)
            return Response({"Bienvenido": True})
        return Response({"Bienvenido": False})

class LogoutAPI(views.APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated, AccesoPerfil)
    def get(self, request):
        logout(request)
        return Response({"Adiós":True})