from nftgram.models import Profile
from nftgram.serializers import ProfileSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [IsAuthenticated]
