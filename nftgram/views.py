from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework import generics, viewsets
from rest_framework.reverse import reverse
from rest_framework.response import Response
from nftgram.models import  User, NFTs, Relations
from nftgram.serializers import AllNFTsSerializer, UserSerializer, NFTSerializer, UserCreateSerializer, UserFollowSerializer, FollowNFTSerializer
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from .permissions import IsFollowOrReadOnly

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


# @csrf_exempt
# def user_list(request):
#     if request.method == 'GET':
#         users = User.objects.all()
#         user_serializer = UserSerializer(users, many=True)
#         return JSONResponse(user_serializer.data)

#     elif request.method == 'NFT':
#         user_data = JSONParser().parse(request)
#         user_serializer = UserSerializer(data=user_data)
#         if user_serializer.is_valid():
#             user_serializer.save()
#             return JSONResponse(user_serializer.data, status=status.HTTP_201_CREATED)
#         return JSONResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
# def user_detail(request, user_id):
#     try:
#         user = User.objects.get(pk=user_id)
#     except User.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         user_serializer = UserSerializer(user)
#         return JSONResponse(user_serializer.data)

#     elif request.method == 'PUT':
#         user_data = JSONParser().parse(request)
#         user_serializer = UserSerializer(user, data=user_data)
#         if user_serializer.is_valid():
#             user_serializer.save()
#             return JSONResponse(user_serializer.data)
#         return JSONResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         user.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# @csrf_exempt
# def NFT_list(request):
#     if request.method == 'GET':
#         NFTs = NFT.objects.all()
#         NFT_serializer = UserSerializer(NFTs, many=True)
#         return JSONResponse(NFT_serializer.data)

#     elif request.method == 'NFT':
#         NFT_data = JSONParser().parse(request)
#         NFT_serializer = NFTSerializer(data=NFT_data)
#         if NFT_serializer.is_valid():
#             NFT_serializer.save()
#             return JSONResponse(NFT_serializer.data, status=status.HTTP_201_CREATED)
#         return JSONResponse(NFT_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
# def NFT_detail(request, NFT_id):
#     try:
#         NFT = NFT.objects.get(pk=NFT_id)
#     except NFT.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         NFT_serializer = NFTSerializer(NFT)
#         return JSONResponse(NFT_serializer.data)

#     elif request.method == 'PUT':
#         NFT_data = JSONParser().parse(request)
#         NFT_serializer = UserSerializer(NFT, data=NFT_data)
#         if NFT_serializer.is_valid():
#             NFT_serializer.save()
#             return JSONResponse(NFT_serializer.data)
#         return JSONResponse(NFT_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         NFT.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class NFTList(generics.ListCreateAPIView):
    queryset = NFTs.objects.all()
    serializer_class = NFTSerializer
    name = 'NFTs'

    permissions_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsFollowOrReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class NFTDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NFTs.objects.all()
    serializer_class = NFTSerializer
    name = 'nfts-detail'

    permissions_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsFollowOrReadOnly
    )

class FollowList(generics.ListCreateAPIView):
    queryset = Relations.objects.all()
    serializer_class = UserFollowSerializer
    name = 'follows'

    permissions_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsFollowOrReadOnly
    )

class AllNFTs(generics.ListAPIView):
    queryset = NFTs.objects.all()
    serializer_class = AllNFTsSerializer
    name = 'follow-NFT-list'

class FollowDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Relations.objects.all()
    serializer_class = FollowNFTSerializer
    name = 'relation-detail'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsFollowOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = (AllowAny,)
    name = 'user-create'

class UserCreateDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    name = 'user-create-details'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'Signup':reverse(UserCreate.name, request=request),
            'NFTs': reverse(NFTList.name, request=request),
            'All NFTs': reverse(AllNFTs.name, request=request),
            'Followers':reverse(FollowList.name, request=request),
            'Users':reverse(UserList.name, request=request),
            })
