from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile, Task
from .serializers import UserProfileSerializer, TaskSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['status', 'assigned_to__user__username']
