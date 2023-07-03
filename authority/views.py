from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView

from authority.models import User
from authority.permisions import IsUser
from authority.serializers import CustomTokenObtainPairSerializer, UserCreateSerializer, UsersSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsUser]


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
