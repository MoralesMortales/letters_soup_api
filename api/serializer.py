from rest_framework import serializers
from .models import * 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_app
        fields = ['id', 'email', 'password', 'is_admin']  

    def create(self, validated_data):
        new_user = User_app.objects.create(
            email=validated_data['email'],
            password=validated_data['password'] 
        )
        return new_user

class SoupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soup
        fields = ['id', 'email', 'row', 'col', 'soup', 'words']
