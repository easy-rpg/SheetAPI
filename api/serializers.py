from rest_framework.serializers import ModelSerializer, Serializer, CharField
from django.contrib.auth.models import User


class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'username', 'email', 'first_name', 'last_name']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class PasswordSerializer(Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = CharField(required=True)
    new_password = CharField(required=True)
