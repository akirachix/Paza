
from django.urls import path, include
from rest_framework import routers
from .views import LeaderViewSet, UserViewSet, ResidentViewSet, PostsViewSet
from knox import views as knox_views
from .views import LoginAPI
from django.urls import path






router = routers.DefaultRouter()
router.register(r"User", UserViewSet)
router.register(r"leader", LeaderViewSet)
router.register(r"resident", ResidentViewSet)
router.register(r"posts", PostsViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path('login/', LoginAPI.as_view(), name='login'),

    

]

