
from django.urls import path, include
from rest_framework import routers


from .views import ForumViewSet, LeaderViewSet, UserViewSet, ResidentViewSet, PostsViewSet,CommentViewSet,ForumSerializer
from knox import views as knox_views
from .views import LoginAPI
from django.urls import path






router = routers.DefaultRouter()
router.register(r"User", UserViewSet)
router.register(r"leader", LeaderViewSet)
router.register(r"resident", ResidentViewSet)
router.register(r"posts", PostsViewSet)
router.register(r"comments", CommentViewSet)
router.register(r"forums",ForumViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginAPI.as_view(), name='login'),
   
    

]

