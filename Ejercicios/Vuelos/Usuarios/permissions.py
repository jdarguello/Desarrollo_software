#Gestión de permisos personalizados

from rest_framework.permissions import BasePermission

class AccesoPersonal(BasePermission):
    def has_object_permission(self, request, view, obj):
        #request => contiene TODA la información del usuario que desea manipular un objeto

        #view => clase de API que se quiere manipular

        #obj => hace referencia al objeto CRUD que se desea manipular


        #request.user => es un objeto de tipo 'Usuario'

        if request.user.is_superuser:
            return True #=> se brinda permiso para manipular objetos