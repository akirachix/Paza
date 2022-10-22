from rest_framework import serializers
from django.contrib.auth.models import User

from . import models
from paza import models


class LeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model =models .Leader
        fields=['first_name','last_name','username','password', 'county','neighbourhood_associattion',]
        
        
class LeaderRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Leader
        fields = ( 'first_name', 'last_name', 'username','password', 'county','neighbourhood_associattion',)
        extra_kwargs = {'password': {'write_only': True}}
        
def create(self, validated_data):
        user = models.Leader.objects.create(validated_data['username'], validated_data['password'],)
        return user



class ResidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Resident
        fields=['first_name', 'last_name','username', 'password','neighbourhood_associattion','county',]


# Register Serializer
class ResidentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Resident
        fields = ( 'first_name', 'last_name', 'username','password','neighbourhood_associattion','county')
        extra_kwargs = {'password': {'write_only': True}}
def create(self, validated_data):
        user = models.Resident.objects.create(validated_data['username'], validated_data['password'],)
        return user


#Posts Serializer
class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Posts
        fields=['tittle','description','image','sector','video']


#comments Serializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields=['tittle','description','image','sector', 'video','time_date',]

