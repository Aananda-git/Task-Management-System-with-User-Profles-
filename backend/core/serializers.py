from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Task


class UserProfileCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'bio', 'profile_picture']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken.")
        return value

    def create(self, validated_data):
        username = validated_data.pop('username')
        email = validated_data.pop('email')

        # Create user without password
        user = User.objects.create(username=username, email=email)
        
        profile = UserProfile.objects.create(user=user, **validated_data)
        return profile


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'bio', 'profile_picture']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate_status(self, value):
        allowed = ['PENDING', 'IN_PROGRESS', 'COMPLETED']
        if value not in allowed:
            raise serializers.ValidationError("Invalid status.")
        return value
