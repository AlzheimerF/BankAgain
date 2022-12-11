from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Profile, Info, SecretInfo, Rate
from .serializers import ProfileSerializer, InfoSerializer, SecretInfoSerializer, RateSerializer, VerifySerializer


class ProfileRetrieveAPIView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        profile = self.request.user
        return profile


class ProfileViewSet(viewsets.ModelViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [AllowAny, ]

    @action(detail=True, methods=['get'])
    def check_user(self, request, *args, **kwargs):
        user = Profile.objects.get(id=kwargs.get('pk'))

        serializer1 = ProfileSerializer(user)

        info = request.user.info
        serializer2 = InfoSerializer(info)

        secret_info = SecretInfo.objects.get(user=kwargs.get('pk'))
        serializer3 = SecretInfoSerializer(secret_info)

        return Response([serializer1.data, serializer2.data, serializer3.data])

class EmailVerifyAPIView(generics.RetrieveAPIView):
    serializer_class = VerifySerializer
    queryset = Profile.objects.filter(is_active=False)

    lookup_field = 'email_verify'
    permission_classes = (AllowAny, )

    def retrieve(self, request, *args, **kwargs):
        instance: Profile = self.get_object()
        serializer = self.get_serializer(instance)
        instance.email_verificate()
        return Response(serializer.data)

class InfoViewSet(viewsets.ModelViewSet):

    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    permission_classes = [AllowAny, ]

class SecretInfoViewSet(viewsets.ModelViewSet):

    queryset = SecretInfo.objects.all()
    serializer_class = SecretInfoSerializer
    permission_classes = [AllowAny, ]


class RateViewSet(viewsets.ModelViewSet):

    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    permission_classes = [AllowAny, ]

