from rest_framework import serializers
from .models import * 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_app 
        fields = '__all__'

    def create(self, validated_data):
        # Crea el usuario con un hash para la contraseña
        new_user = User_app.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'])
        return new_user
