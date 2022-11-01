

from paza.models import Forum, Leader, Resident, Posts, Resident,Comment
from rest_framework import serializers
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password")


class LeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leader
        fields = ("first_name", "last_name", "county", "password","neighbourhood_associattion","username")


class ResidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = ("first_name", "last_name", "county", "password","neighbourhood_associattion","username")


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('image_name','image_caption','created','image','author', 'likes')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('body','created','post','author',)


class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = ('tittle','description','date_created','topic','name')

        






    

    















