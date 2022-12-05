from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import SecretInfoViewSet

router = DefaultRouter()
router.register('', SecretInfoViewSet, basename='secret_info')

urlpatterns = router.urls