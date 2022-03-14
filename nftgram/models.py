from pyexpat import model
from django.db import models
from django.contrib.auth.models import User # AbstractBaseUser, BaseUserManager, PermissionsMixin


# class UserManager(BaseUserManager):
#     use_in_migrations = True

#     # Method to save user to the database
#     def save_user(self, username, password, **extra_fields):
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, username, password=None, **extra_fields):
#         extra_fields['is_admin'] = False
#         clean_username = User.clean(username)
#         return self.save_user(username=clean_username, password=password, **extra_fields)

#     def create_superuser(self, username, password, **extra_fields):
#         extra_fields.setdefault('is_admin', True)
#         if extra_fields.get('is_admin') is not True: raise ValueError('is_admin should be True')
#         return self.save_user(username, password, **extra_fields)


# class User(AbstractBaseUser, PermissionsMixin):
#     objects = UserManager()
#     id = models.BigAutoField(primary_key=True)
#     username = models.CharField(max_length=60, unique=True)
#     email = models.EmailField(max_length=255, unique=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     last_login = models.DateTimeField(auto_now=True)
#     USERNAME_FIELD = 'username'


#     @property
#     def is_staff(self):
#         return self.is_admin

#     @property
#     def is_superuser(self):
#         return self.is_admin

#     class Meta:
#         db_table = "users"


# class Post(models.Model):
#     post_id = models.AutoField(primary_key=True)
#     user_id = models.CharField(max_length=200)
#     title = models.CharField(max_length=50, blank=False, default='')
#     description = models.CharField(max_length=200)
#     posted_at = models.DateTimeField(auto_now_add=True)
#     nft_id = models.IntegerField()
#     nft_url = models.CharField(max_length=255)

#     class Meta:
#         db_table = "post"


# class Reply(models.Model):

#     reply_id = models.AutoField(primary_key=True)
#     user_id = models.CharField(max_length=200)
#     post_id = models.IntegerField()
#     replied_at = models.DateTimeField(auto_now_add=True)
#     reply_text = models.CharField(max_length=200)

#     class Meta:
#         db_table = "reply"


# class UserProfile(models.Model):

#     user_id = models.CharField(max_length=200)
#     name = models.CharField(max_length=200)
#     profile_heading = models.CharField(max_length=50)
#     profile_description = models.CharField(max_length=200)
#     profile_pic_url = models.CharField(max_length=255)

#     class Meta:
#         db_table = "userprofile"


# class Follows(models.Model):

#     user_id = models.IntegerField()
#     follows_id = models.IntegerField()

#     class Meta:
#         db_table = "follows"

class Posts(models.Model):
    author = models.ForeignKey(
        'auth.User',
        related_name='tweets',
        on_delete=models.CASCADE,
    )
    post_text = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('post_text',)

    def __str__(self):
        return self.post_text


class Relations(models.Model):
    follower = models.ForeignKey(  
        'auth.User',            
        related_name='relations',
        on_delete=models.CASCADE)
    followed = models.ForeignKey(  
        User,            
        related_name='followed',
        on_delete=models.CASCADE)
    
    def __unicode__(self):
        return u"%s is following %s" % (self.follower.username, 
            self.followed.username)
    
    def save(self, **kwargs):

        if self.follower == self.followed:
            raise ValueError("Cannot follow yourself.")
        super(Relations, self).save(**kwargs)

    class Meta:
        unique_together = (('followed','follower'),)