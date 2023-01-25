from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer, UserCreateSerializer, UserCreatePasswordRetypeSerializer
from rest_framework import serializers
from djoser.conf import settings

from accounts.models import CustomUser


class UserRegistrationSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = (
            'name', 'phone', 'city', 'email', 'money', 'password',
        )


class UserAPISerializer(UserSerializer, serializers.Serializer):
    class Meta(UserSerializer.Meta):
        fields = (
            'id', 'name', 'phone', 'city', 'email',
        )


class UserAPICreatePasswordRetypeSerializer(UserCreatePasswordRetypeSerializer):
    class Meta(UserCreatePasswordRetypeSerializer.Meta):
        fields = (
            'name', 'phone', 'city', 'email', 'money', 'password',
        )


class UserTopMoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'name', 'money',
        )
