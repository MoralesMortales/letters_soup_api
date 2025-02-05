
from rest_framework import viewsets, status
from rest_framework.views import APIView
from .models import User_app, Soup
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
        data = request.data

        try:
            user = User_app.objects.get(email=data.get('email'))
        except User_app.DoesNotExist:
            raise NotFound("El usuario con el email proporcionado no existe.")

        data['email'] = user.id 

        serializer = SoupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserSoupListView(APIView):

    def get(self, request, user_id, *args, **kwargs):
        try:
            user = User_app.objects.get(id=user_id)
        except User_app.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        
        soups = Soup.objects.filter(email=user)
        
        if not soups:
            return Response({"detail": "No soups found for this user."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SoupSerializer(soups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserSoupDetailView(APIView):

    def get(self, request, user_id, soup_id, *args, **kwargs):
        try:
            user = User_app.objects.get(id=user_id)
        except User_app.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            soup = Soup.objects.get(id=soup_id, email=user)
        except Soup.DoesNotExist:
            return Response({"detail": "Soup not found for this user."}, status=status.HTTP_404_NOT_FOUND)

        serializer = SoupSerializer(soup)
        return Response(serializer.data, status=status.HTTP_200_OK)
