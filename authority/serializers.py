from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from animals.serializers import AnimalSerializer
from authority.models import User


class UserCreateSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'password',
        )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['role'] = user.role

        return token


class UsersSerializer(serializers.ModelSerializer):

    animals = AnimalSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'animals')
