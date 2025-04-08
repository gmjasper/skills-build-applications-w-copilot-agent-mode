from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from .models import User, Team, Activity, Leaderboard, Workout

@api_view(['GET'])
def api_root(request, format=None):
    base_urls = [
        'http://localhost:8000/',
        'https://cautious-invention-8000-465rxg76v6x27v5j.app.github.dev/'
    ]
    return Response({
        'users': [url + 'api/users/' for url in base_urls],
        'teams': [url + 'api/teams/' for url in base_urls],
        'activities': [url + 'api/activities/' for url in base_urls],
        'leaderboard': [url + 'api/leaderboard/' for url in base_urls],
        'workouts': [url + 'api/workouts/' for url in base_urls]
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
