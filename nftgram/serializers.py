from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Posts, Relations
# from nftgram.models import Reply
# from nftgram.models import UserProfile
# from nftgram.models import Follows

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#     username = serializers.CharField(max_length=60)
#     password = serializers.CharField(max_length=200)
#     date_joined = serializers.DateTimeField(read_only=True)
#     last_login = serializers.DateTimeField()

#     # create function creates and return an object from validated JSON data
#     def create(self, validated_data):
#         return User.objects.create(**validated_data)

#     # update function updates an object instance from validated JSON data
#     def update(self, instance, validated_data):
#         instance.username = validated_data.get('username', instance.username)
#         instance.password = validated_data.get('password', instance.password)
#         instance.name = validated_data.get('username', instance.name)
#         instance.roles = validated_data.get('roles', instance.roles)
#         instance.date_joined = validated_data.get('date_joined', instance.date_joined)
#         instance.save()
#         return instance

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'password', 'date_joined', 'last_login']


# class PostSerializer(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model = Post
#         fields = (
#             'post_id',
#             'user_id',
#             'title',
#             'description',
#             'posted_at',
#             'nft_id',
#             'nft_url',
#             )


# class ReplySerializer(serializers.HyperlinkedModelSerializer):
#     user_id = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
#     post_id = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='name')
#     class Meta:

#         model = Reply
#         fields = (
#             'reply_id',
#             'user_id',
#             'post_id',
#             'replied_at',
#             'reply_text',
#             )


# class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
#     user_id = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
#     name = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

#     class Meta:
#         model = UserProfile
#         fields = (
#             'user_id',
#             'name',
#             'profile_heading',
#             'gender_description',
#             'profile_description',
#             'profile_pic_url',
#             )


# class FollowsSerializer(serializers.ModelSerializer):
#     user_id = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

#     class Meta:
#         model = Follows
#         fields = (
#             'user_id',
#             'follows_id',
#             )

class PostSerializer(serializers.HyperlinkedModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Posts
        fields = (
                'url',
                'author',
                'post_text',
                'date')

class UserPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = (
            'url',
            'post_text')

class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class FollowSerializer(serializers.HyperlinkedModelSerializer):

    follower = serializers.ReadOnlyField(source='follower.username')

    followed = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Relations
        fields = (
                'url',
                'follower',
                'followed')

class UserFollowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Relations
        fields = (
                'url',
                'followed')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = UserPostSerializer(many=True, read_only=True)
    follow = UserFollowSerializer (many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'url', 
            'pk',
            'username',
            'posts',
            'follow')

class FollowPostSerializer(serializers.HyperlinkedModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Posts
        fields = (
                'url',
                'author',
                'post_text',
                'date')