#Construcción de serialzacdores

from rest_framework import serializers

from Usuarios.models import *

class UsuarioSerial (serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {
                'write_only':True,
                'style': {
                    'input_type': 'password'
                }
            }
        }

class PerfilSerial (serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'