from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import ProfileViewSet, InfoViewSet, RateViewSet, SecretInfoViewSet


router = DefaultRouter()
router.register('user', ProfileViewSet, basename='user')
router.register('rate', RateViewSet, basename='rate')
router.register('info', InfoViewSet, basename='info_user')
router.register('secret_info', SecretInfoViewSet, basename='secret_info')


urlpatterns = [
    path('', include(router.urls)),
]
