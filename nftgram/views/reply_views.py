from nftgram.models import Reply
from nftgram.serializers import ReplySerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    # permission_classes = [IsAuthenticated]