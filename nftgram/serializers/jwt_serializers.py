from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class JwtTokenObtainPairSerializer(TokenObtainPairSerializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    @classmethod
    def get_token(cls, user):
        token = super(JwtTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        return token

