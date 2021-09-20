from django.db.models import fields
from rest_framework import serializers

from .models import *

class UserSerial (serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password':{'write_only':True}}

class PerfilSerial (serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'
