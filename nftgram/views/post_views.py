from nftgram.models import Post
from nftgram.serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
