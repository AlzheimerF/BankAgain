from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import ProfileViewSet, InfoViewSet

router = DefaultRouter()
router.register('', ProfileViewSet, basename='user')

urlpatterns = router.urls