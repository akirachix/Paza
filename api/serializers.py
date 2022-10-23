

from paza.models import  Forum, Leader, Resident, Posts, Resident,Comment
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
        fields = ("tittle", "description", "sector", "image","time_date","video")

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("head", "description", "sector","time_date")


class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = ("tittle", "description", "moderator","time_date")






    

    















