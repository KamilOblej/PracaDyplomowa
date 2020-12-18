from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password  # Register serializer
from camera.models import Temperature, Thermo, Photo


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name')
        # extra_kwargs = {
        #     'password': {'write_only': True},
        # }

        def create(self, validated_data):
            user = User.objects.create_user(validated_data['username'], password=validated_data['password'],
                                            first_name=validated_data['first_name'],  last_name=validated_data['last_name'], is_active=True)
            return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = '__all__'
        # exclude = ['date_taken']

class ThermoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thermo
        # exclude = ['name']
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        # exclude = ['name']
        fields = '__all__'





