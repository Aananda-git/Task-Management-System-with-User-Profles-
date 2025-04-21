from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserProfileViewSet,
    TaskViewSet,
    CreateUserProfileView,
)

router = DefaultRouter()
router.register('profiles', UserProfileViewSet, basename='profiles')
router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
    path('create-profile/', CreateUserProfileView.as_view(), name='create-profile'),
]
