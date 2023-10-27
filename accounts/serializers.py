from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer
from .models import CustomUser




class CustomLoginSerializer(LoginSerializer):
    email = None
    username = serializers.CharField(required=True)


class CustomUserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name']
