from nftgram.models import Follows
from nftgram.models import User
from rest_framework import serializers


class FollowsSerializer(serializers.ModelSerializer):
    user_id = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Follows
        fields = (
            'user_id',
            'follows_id',
            )
