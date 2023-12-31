from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import User


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password')

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'phone', 'user_blocked','user_type','name','store','store_location')




