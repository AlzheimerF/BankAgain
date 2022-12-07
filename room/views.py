from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, permissions

from .consumers import ChatConsumer
from . import models, serializers


class RoomViewSet(viewsets.ModelViewSet):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer
    permission_classes = [permissions.AllowAny]

