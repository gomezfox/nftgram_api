from rest_framework import serializers
from nftgram.models import Reply
from nftgram.models import User
from nftgram.models import Post


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