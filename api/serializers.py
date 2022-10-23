from rest_framework import serializers
from django.contrib.auth.models import User

from paza import models


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user


class LeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Leader
        fields=['first_name', 'last_name','username', 'password',]       


        
class LeaderRegisterModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Leader
        fields = ['first_name', 'last_name', 'username','password']
        extra_kwargs = {'password': {'write_only': True}}
        
def create(self, validated_data):
        user = models.Leader.objects.create(validated_data['username'], validated_data['password'],)
        return user

class ResidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Resident
        fields=['first_name', 'last_name','username', 'password',]


# Register Serializer
class ResidentRegisterModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Resident
        fields = ['first_name', 'last_name', 'username','password',]
        extra_kwargs = {'password': {'write_only': True}}
def create(self, validated_data):
        user = models.Resident.objects.create(validated_data['username'], validated_data['password'],)
        return user

#Posts Serializer
class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Posts
        fields=['tittle','description','image',]





