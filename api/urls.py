from django.urls import path
from . import views


urlpatterns = [
    path('leaders/',views.LeaderRegisterViewSet.as_view(), name='leaders' ),
    path('login/', views.LoginAPI.as_view(), name='login'),
    path('residents/',views.ResidentRegisterViewset.as_view(),name='residents'),
    path('posts/',views.PostsViewset.as_view(),name='posts'),
    path('comments/',views.CommentViewset.as_view(),name='comments'),


]