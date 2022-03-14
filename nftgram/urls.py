from django.urls import path, re_path, include
from nftgram.views import UserViewSet, PostViewSet, ProfileViewSet, FollowsViewSet, ReplyViewSet, APILogoutView
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'follows', FollowsViewSet)
router.register(r'replies', ReplyViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout_token/', APILogoutView.as_view(), name='logout_token'),
]
