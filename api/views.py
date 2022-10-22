from pydoc import visiblename
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from paza import models
from .serializers import *
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from . import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import generics, permissions, viewsets
from django.contrib.auth import login,authenticate
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken




class LeaderRegisterViewSet(generics.GenericAPIView):
    serializer_class = serializers.LeaderRegisterSerializer
    queryset =  models.Leader.objects.all()

    def post(self, request,format=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        leader = serializer.save()
        models.Leader.objects.create_user(username=leader.username , password=leader.password)
        return Response({
        # "leader": serializers.LeaderSerializer(leader, context=self.get_serializer_context()).data,
        })

    def get(self, request, *args, **kwargs):
        leaders = models.Leader.objects.all()
        leader_serializer=serializers.LeaderSerializer(leaders,many=True)
        return JsonResponse(leader_serializer.data,safe=False)



class ResidentRegisterViewset(generics.GenericAPIView):
    serializer_class = serializers.ResidentSerializer
    queryset =  models.Resident.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        resident = serializer.save()
        User.objects.create_user(username=resident.username , password=resident.password)
        return Response({
        "resident": serializers.ResidentSerializer(resident, context=self.get_serializer_context()).data,
        })

    def get(self, request, *args, **kwargs):
        resident = models.Resident.objects.all()
        resident_serializer=serializers.ResidentSerializer(resident,many=True)
        return JsonResponse(resident_serializer.data,safe=False)


class PostsViewset(generics.GenericAPIView): 
    def get(self, request, *args, **kwargs):
        posts = models.Posts.objects.all()
        post_serializer=serializers.PostsSerializer(posts,many=True)
        return JsonResponse(post_serializer.data,safe=False)


class CommentViewset(generics.GenericAPIView): 
    def get(self, request, *args, **kwargs):
        posts = models.Comment.objects.all()
        post_serializer=serializers.CommentSerializer(posts,many=True)
        return JsonResponse(post_serializer.data,safe=False)        



# Register API
class LoginAPI(ObtainAuthToken):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, ):
        username=request.data['username']
        password=request.data['password']
        user=authenticate(request,username=username, password=password)
        print(user)
        token, _=Token.objects.get_or_create(user=user)
        return Response({
            'body': 'login successful',
            "token": token.key
        })




