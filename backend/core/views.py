from rest_framework import viewsets, status, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile, Task
from .serializers import (
    UserProfileSerializer,
    UserProfileCreateSerializer,
    TaskSerializer
)


class CreateUserProfileView(APIView):
    """
    Custom endpoint to create a user with username, email,
    and associate a profile (bio, profile picture).
    """
    def post(self, request):
        serializer = UserProfileCreateSerializer(data=request.data)
        if serializer.is_valid():
            profile = serializer.save()
            return Response({
                'message': 'User profile created successfully.',
                'profile': UserProfileSerializer(profile).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    Full CRUD on user profiles (excluding user account changes).
    """
    queryset = UserProfile.objects.select_related('user').all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['status', 'assigned_to']  
