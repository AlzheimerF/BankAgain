from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Profile, Info, SecretInfo, Rate
from .serializers import ProfileSerializer, InfoSerializer, SecretInfoSerializer

class ProfileViewSet(viewsets.ModelViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [AllowAny, ]

    @action(detail=True, methods=['get'])
    def check_user(self, request, *args, **kwargs):

        user = Profile.objects.get(id=kwargs.get('pk'))

        serializer1 = ProfileSerializer(user)

        info = Info.objects.get(user=kwargs.get('pk'))
        serializer2 = InfoSerializer(info)

        secret_info = SecretInfo.objects.get(user=kwargs.get('pk'))
        serializer3 = SecretInfoSerializer(secret_info)

        return Response([serializer1.data, serializer2.data, serializer3.data])


class InfoViewSet(viewsets.ModelViewSet):

    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    permission_classes = [IsAdminUser, ]

class SecretInfoViewSet(viewsets.ModelViewSet):

    queryset = SecretInfo.objects.all()
    serializer_class = SecretInfoSerializer
    permission_classes = [IsAdminUser, ]

    def create(self, request, *args, **kwargs):
        print(request.data)