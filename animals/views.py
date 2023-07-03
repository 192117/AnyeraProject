from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from animals.models import Animals
from animals.serializers import AnimalSerializer
from authority.permisions import IsOwner, IsUser


class AnimalsListView(generics.ListAPIView):
    queryset = Animals.objects.all()
    serializer_class = AnimalSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['kind_of_animal']


class AnimalCreateView(generics.CreateAPIView):
    queryset = Animals.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [IsUser]


class AnimalsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animals.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [IsOwner]
