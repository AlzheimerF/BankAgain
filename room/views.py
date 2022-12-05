from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, permissions

from .consumers import ChatConsumer
from . import models, serializers


class RoomViewSet(viewsets.ModelViewSet):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer
    permission_classes = [permissions.AllowAny]

    # @action(['POST'], detail=True, url_path='send_message')
    # def send_message(self, request, *args, **kwargs):
    #     ChatConsumer()
    #     return Response({'ok': True})
    #
