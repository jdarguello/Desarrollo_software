from rest_framework import viewsets #=> manipulación CRUD -> bases de datos
from rest_framework import authentication, permissions

from Usuarios.serializers import *
from Usuarios.permissions import *

class UsuarioAPI (viewsets.ModelViewSet):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (AccesoPersonal,)
    serializer_class = UsuarioSerial
    queryset = get_user_model().objects.all()

class PerfilAPI (viewsets.ModelViewSet):
    serializer_class = PerfilSerial
    queryset = Perfil.objects.all()


from rest_framework import views
from rest_framework.response import Response

from django.contrib.auth import logout, login
from django.shortcuts import get_object_or_404

class LogoutAPI (views.APIView):
    def get(self, request):
        logout(request)
        return Response("Se ha hecho logout")

class LoginAPI (views.APIView):
    def post(self, request):
        #request => obtener TODA la información de nuestros usuarios
        #request.user => objeto de tipo usuario
        if 'username' in request.data and 'password' in request.data:
            usuario = get_object_or_404(get_user_model(), username = request.data['username'])
            if usuario.check_password(request.data['password']):
                login(request, usuario)
                return Response("El usuario " + usuario.username + " ha hecho login")
            return Response("Nombre de usuario o contraseña incorrecta")
        return Response("Datos incorrectos")
