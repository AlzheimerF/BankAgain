from rest_framework import serializers
from .models import Profile, Info, SecretInfo, Rate

class ProfileSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'username', 'password', 'password2', 'date_joined', ]

    def validate(self, attrs):
        if attrs['password2'] != attrs['password']:
            raise serializers.ValidationError()
        return attrs

    def create(self, validated_data):
        profile = Profile.objects.create_user(
            username=validated_data.get('username'),
            password=validated_data.get('password'),
            about_yourself=validated_data.get('about_yourself')
        )

        return profile


class InfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Info
        fields = ['user', 'country', 'city', 'language', 'age', 'gender', ]

    def create(self, validated_data):
        info = Info.objects.create(
            user=validated_data.get('user'),
            country=validated_data.get('country'),
            city=validated_data.get('city'),
            language=validated_data.get('language'),
            age=validated_data.get('age'),
            gender=validated_data.get('gender')
        )
        return info

class SecretInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = SecretInfo
        fields = '__all__'

    def create(self, validated_data):
        secret_info = SecretInfo.objects.create(
            user=validated_data.get('user'),
            passport_front=validated_data.get('passport_front'),
            passport_back=validated_data.get('passport_back'),
            address=validated_data.get('address'),
            number=validated_data.get('number')
        )
        return secret_info

class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = '__all__'
