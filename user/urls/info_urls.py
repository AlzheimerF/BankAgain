from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import ProfileViewSet, InfoViewSet, SecretInfoViewSet

router = DefaultRouter()
router.register('', InfoViewSet, basename='info_user')
router.register('', SecretInfoViewSet, basename='secret_info')

urlpatterns = router.urls