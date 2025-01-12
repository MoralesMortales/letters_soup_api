
from rest_framework import viewsets
from .models import User_app
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

class UserViewSet(viewsets.ModelViewSet):
    queryset = User_app.objects.all()
    serializer_class = UserSerializer
