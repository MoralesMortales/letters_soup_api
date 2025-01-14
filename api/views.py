
from rest_framework import viewsets, status
from rest_framework.views import APIView
from .models import User_app
from .serializer import UserSerializer
from rest_framework.response import Response 
from rest_framework.exceptions import NotFound

class UserViewSet(viewsets.ModelViewSet):
    queryset = User_app.objects.all()
    serializer_class = UserSerializer

class UserCreateView(APIView):
    def post(self, request):
        print('corriendo')
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
