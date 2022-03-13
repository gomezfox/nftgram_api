from rest_framework import serializers
from nftgram.models import User
from nftgram.models import Post
from nftgram.models import Reply
from nftgram.models import UserProfile
from nftgram.models import Follows
from nftgram.models import Auth

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User   
        fields = (
            'id',
            'username',
            'password',
            'name',
            'roles',
            'date_joined',
            )

class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = (
            'post_id',
            'user_id',
            'title',
            'description',
            'posted_at',
            'nft_id',
            'nft_url',
            )

class ReplySerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    post_id = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='name')
    class Meta:
        model = Reply
        fields = (
            'reply_id',
            'user_id',
            'post_id',
            'replied_at',
            'reply_text',
            )

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    name = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = UserProfile
        fields = (
            'user_id',
            'name',
            'profile_heading',
            'gender_description',
            'profile_description',
            'profile_pic_url',
            )

class FollowsSerializer(serializers.ModelSerializer):
    user_id = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Follows
        fields = (
            'user_id',
            'follows_id',
            )

class AuthSerializer(serializers.ModelSerializer):
    user_id = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Auth
        fields = (
            'user_id',
            'token',
            'role'
            )


