from rest_framework import serializers
from .models import * 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_app
        fields = ['id', 'email', 'password', 'is_admin']  # Puedes incluir solo los campos que quieras permitir

    def create(self, validated_data):
        # Crea el usuario (puedes agregar hash de la contraseña si es necesario)
        new_user = User_app.objects.create(
            email=validated_data['email'],
            password=validated_data['password']  # Asegúrate de manejar la seguridad de las contraseñas
        )
        return new_user

class SoupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soup
        fields = ['id', 'email', 'row', 'col', 'soup', 'words']
