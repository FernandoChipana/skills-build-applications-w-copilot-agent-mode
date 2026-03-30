"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TeamViewSet, ActivityViewSet, LeaderboardViewSet, WorkoutViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
import os

CODESPACE_NAME = os.environ.get('CODESPACE_NAME')
if CODESPACE_NAME:
    BASE_URL = f"https://{CODESPACE_NAME}-8000.app.github.dev"
else:
    BASE_URL = "http://localhost:8000"

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': f"{BASE_URL}{reverse('user-list', request=request, format=format)}",
        'teams': f"{BASE_URL}{reverse('team-list', request=request, format=format)}",
        'activities': f"{BASE_URL}{reverse('activity-list', request=request, format=format)}",
        'leaderboard': f"{BASE_URL}{reverse('leaderboard-list', request=request, format=format)}",
        'workouts': f"{BASE_URL}{reverse('workout-list', request=request, format=format)}",
    })

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')
router.register(r'workouts', WorkoutViewSet, basename='workout')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', api_root, name='api-root'),
]
