from django.urls import re_path
from . import views
# from nftgram.views import UserViewSet
# from rest_framework import routers
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
#     path('', include(router.urls)),
#     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^users/$', views.UserList.as_view(), name=views.UserList.name),
    re_path(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name=views.UserDetail.name),
    re_path(r'^account/register/$', views.UserCreate.as_view(), name=views.UserCreate.name),
    re_path(r'^account/register/(?P<pk>[0-9]+)/$', views.UserCreateDetail.as_view(), name=views.UserCreateDetail.name),
    re_path(r'^follow/$', views.FollowList.as_view(), name=views.FollowList.name),
    re_path(r'^follow/(?P<pk>[0-9]+)/$', views.FollowDetail.as_view(), name=views.FollowDetail.name),
    re_path(r'^posts/$', views.PostList.as_view(),name=views.PostList.name),
    re_path(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name=views.PostDetail.name),
    re_path(r'^allposts/$', views.AllPosts.as_view(), name=views.AllPosts.name),
    re_path(r'^$', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]