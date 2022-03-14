from rest_framework import serializers
from nftgram.models import Post


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
