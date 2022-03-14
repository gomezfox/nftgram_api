from rest_framework import serializers
from nftgram.models import Profile
from nftgram.models import User


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Profile
        fields = (
            'user_id',
            'name',
            'profile_heading',
            'gender_description',
            'profile_description',
            'profile_pic_url',
        )
