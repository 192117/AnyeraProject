from rest_framework import serializers

from animals.models import Animals


class AnimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Animals
        fields = ('id', 'name', 'age', 'kind_of_animal', 'photo')

    def create(self, validated_data):
        user = self.context['request'].user
        return Animals.objects.create(user=user, **validated_data)
