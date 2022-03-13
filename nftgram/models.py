from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):
    use_in_migrations = True

    # Method to save user to the database
    def save_user(self, username, password, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields['is_admin'] = False
        clean_username = User.clean(username)
        return self.save_user(username=clean_username, password=password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        if extra_fields.get('is_admin') is not True: raise ValueError('is_admin should be True')
        return self.save_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=60, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'username'


    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    class Meta:
        db_table = "users"

