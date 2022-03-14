from django.db import models
from .user_model import User


class Follows(models.Model):

    user_id = models.ManyToManyField(User, related_name="+")
    follows_id = models.ManyToManyField(User, related_name="+")

    class Meta:
        db_table = "follows"
