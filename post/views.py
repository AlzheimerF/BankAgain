from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from . import models
from . import serializers


class PostViewSet(viewsets.ModelViewSet):

    queryset = models.Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = serializers.PostSerializer


# class OrderViewSet(viewsets.ModelViewSet):
#
#     queryset = models.Order.objects.all()