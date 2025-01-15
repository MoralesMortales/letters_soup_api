
from rest_framework import viewsets, status
from rest_framework.views import APIView
from .models import User_app
from .serializer import UserSerializer, SoupSerializer
from rest_framework.response import Response 
from rest_framework.exceptions import NotFound

class UserViewSet(viewsets.ModelViewSet):
    queryset = User_app.objects.all()
    serializer_class = UserSerializer

class UserCreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SoupCreateView(APIView):
    def post(self, request):
        # Obtener los datos del request
        data = request.data

        # Validar si el usuario existe
        try:
            user = User_app.objects.get(email=data.get('email'))
        except User_app.DoesNotExist:
            raise NotFound("El usuario con el email proporcionado no existe.")

        # Agregar automáticamente el usuario relacionado
        data['email'] = user.id  # Pasar la clave primaria del usuario

        # Serializar los datos y crear la sopa
        serializer = SoupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
