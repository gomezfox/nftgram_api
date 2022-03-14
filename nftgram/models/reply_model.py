from django.db import models
from .user_model import User
from .post_model import Post


class Reply(models.Model):

    reply_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    replied_at = models.DateTimeField(auto_now_add=True)
    reply_text = models.CharField(max_length=200)

    class Meta:
        db_table = "replies"


