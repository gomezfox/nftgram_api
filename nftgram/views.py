from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status, generics, viewsets
from nftgram.models import  User, Posts
from nftgram.serializers import UserSerializer, PostSerializer
from rest_framework.permissions import AllowAny
from .permissions import IsAuthorOrReadOnly, IsFollowOrReadOnly
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

#     elif request.method == 'POST':
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
# def post_list(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         post_serializer = UserSerializer(posts, many=True)
#         return JSONResponse(post_serializer.data)

#     elif request.method == 'POST':
#         post_data = JSONParser().parse(request)
#         post_serializer = PostSerializer(data=post_data)
#         if post_serializer.is_valid():
#             post_serializer.save()
#             return JSONResponse(post_serializer.data, status=status.HTTP_201_CREATED)
#         return JSONResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
# def post_detail(request, post_id):
#     try:
#         post = Post.objects.get(pk=post_id)
#     except Post.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         post_serializer = PostSerializer(post)
#         return JSONResponse(post_serializer.data)

#     elif request.method == 'PUT':
#         post_data = JSONParser().parse(request)
#         post_serializer = UserSerializer(post, data=post_data)
#         if post_serializer.is_valid():
#             post_serializer.save()
#             return JSONResponse(post_serializer.data)
#         return JSONResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         post.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    name = 'posts'

    permissions_classes = (
        IsAuthorOrReadOnly,
        IsFollowOrReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    name = 'post-detail'

    permissions_classes = (
        IsAuthorOrReadOnly,
        IsFollowOrReadOnly
    )

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialzer
    name = 'user-list'

class UserDetail(generics.RetrieveAPIView):
    queryset User.objects.all()
    serializer_class = UserSerialzer
    name = 'user-detail'