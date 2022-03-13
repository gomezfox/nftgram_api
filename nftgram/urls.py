from django.urls import path, re_path
from nftgram import views


urlpatterns = [
    re_path(r'^users/$', views.user_list),
    re_path(r'^users/(?P<pk>[0-9]+)/$', views.user_detail),
]