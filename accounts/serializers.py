from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(required = False)
    email = serializers.EmailField(required = True)
    password = serializers.CharField(required = True)

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()