from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, TaskViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('profiles', UserProfileViewSet)
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
