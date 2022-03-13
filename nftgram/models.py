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

class Post(models.Model): 
    post_id = models.AutoField(primary_key=True) 
    user_id = models.CharField(max_length=200) 
    title = models.CharField(max_length=50, blank=False, default='') 
    description = models.CharField(max_length=200) 
    posted_at = models.DateTimeField(auto_now_add=True) 
    nft_id = models.IntegerField()
    nft_url =  #not sure

    class Meta: 
        db_table = "post" 

class Reply(models.Model): 

    reply_id = models.AutoField(primary_key=True)  
    user_id = models.CharField(max_length=200) 
    post_id = = models.IntegerField() 
    replied_at = models.DateTimeField(auto_now_add=True) 
    reply_text = models.CharField(max_length=200) 

    class Meta: 
        db_table = "reply"

class UserProfile(models.Model):  

    user_id = models.CharField(max_length=200) 
    name = models.CharField(max_length=200) 
    profile_heading = models.CharField(max_length=50) 
    profile_description = models.CharField(max_length=200) 
    profile_pic_url = # not sure 

    class Meta: 
        db_table = "userprofile"
 

class Follows(models.Model):  

    user_id = models.IntegerField()     
    follows_id = models.IntegerField() 

    class Meta: 
        db_table = "follows"

class Auth(models.Model):  

    user_id = models.IntegerField() #FK? 
    token = models.CharField(max_length=200) #not sure about token legnth
    role = #? 

    class Meta: 
        db_table = "auth"
