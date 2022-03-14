from nftgram.models import Follows
from nftgram.serializers import FollowsSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class FollowsViewSet(viewsets.ModelViewSet):
    queryset = Follows.objects.all()
    serializer_class = FollowsSerializer
    # permission_classes = [IsAuthenticated]