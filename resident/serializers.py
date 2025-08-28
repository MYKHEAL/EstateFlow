from rest_framework import serializers
from djoser.serializers import  UserCreateSerializer as BaseUserCreateSerializer
from .models import House, User


class HouseSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField()
    class Meta:
        model = House
        fields = ['house_number', 'address']


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'phone']