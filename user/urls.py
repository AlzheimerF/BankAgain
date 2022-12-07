from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import ProfileViewSet, InfoViewSet, RateViewSet, SecretInfoViewSet
from .views import EmailVerifyAPIView

router = DefaultRouter()
router.register('user', ProfileViewSet, basename='user')
router.register('rate', RateViewSet, basename='rate')
router.register('info', InfoViewSet, basename='info_user')
router.register('secret_info', SecretInfoViewSet, basename='secret_info')


urlpatterns = [
    path('', include(router.urls)),
    path('email/verification/<uuid:email_verify>', EmailVerifyAPIView.as_view(), name='emailActivate'),
]
