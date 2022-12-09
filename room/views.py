from rest_framework import viewsets, permissions

from . import models, serializers


class RoomViewSet(viewsets.ModelViewSet):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer
    permission_classes = [permissions.AllowAny]

