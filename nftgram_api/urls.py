"""nftgram_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from nftgram.models import User
from rest_framework import routers, serializers, viewsets
from nftgram.serializers import UserSerializer

from django.urls import re_path
from . import views

admin.autodiscover()


# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User



urlpatterns = [
    path('api/', include('nftgram.urls')),
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    #path('users/', view.UserViewSet.as_view(), name='all users'),
    #path('nfts/', view.PostList.as_view(), name='all nfts'),
    #path('nfts/{(?P<pk>[0-9]+)/$}', view.PostList.as_view(), name='all nfts'),
    re_path(r'^users/$', views.UserList.as_view(), name=views.UserList.name),
    re_path(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name=views.UserDetail.name),
    re_path(r'^account/register/$', views.UserCreate.as_view(), name=views.UserCreate.name),
    re_path(r'^account/register/(?P<pk>[0-9]+)/$', views.UserCreateDetail.as_view(), name=views.UserCreateDetail.name),
    re_path(r'^follow/$', views.FollowList.as_view(), name=views.FollowList.name),
    re_path(r'^follow/(?P<pk>[0-9]+)/$', views.FollowDetail.as_view(), name=views.FollowDetail.name),

]
