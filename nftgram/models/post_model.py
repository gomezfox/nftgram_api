from django.db import models
from .user_model import User


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False, default='NFTGram')
    description = models.CharField(max_length=200)
    posted_at = models.DateTimeField(auto_now_add=True)
    nft_token = models.CharField(max_length=255)
    nft_url = models.CharField(max_length=255)

    class Meta:
        db_table = "posts"


