from django.db import models

# Create your models here.


class User(models.Model):

    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    roles = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user"
