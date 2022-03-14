from rest_framework import serializers
from nftgram.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=60)
    password = serializers.CharField(max_length=200)
    date_joined = serializers.DateTimeField(read_only=True)
    last_login = serializers.DateTimeField()

    # # create function creates and return an object from validated JSON data
    # def create(self, validated_data):
    #     return User.objects.create(**validated_data)
    #
    # # update function updates an object instance from validated JSON data
    # def update(self, instance, validated_data):
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.password = validated_data.get('password', instance.password)
    #     instance.name = validated_data.get('username', instance.name)
    #     instance.roles = validated_data.get('roles', instance.roles)
    #     instance.date_joined = validated_data.get('date_joined', instance.date_joined)
    #     instance.save()
    #     return instance

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'date_joined', 'last_login']