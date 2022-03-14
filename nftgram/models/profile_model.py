from django.db import models
from .user_model import User


class Profile(models.Model):

    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    heading = models.CharField(max_length=80)
    description = models.CharField(max_length=255)
    profile_pic_url = models.CharField(max_length=255)

    class Meta:
        db_table = "profiles"
