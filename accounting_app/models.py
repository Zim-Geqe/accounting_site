from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.models import Group, Permission 
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_superuser(self, password, username, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(password, username, **extra_fields)

    def _create_user(self, password, username, **extra_fields):

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='custom_users',
        related_query_name='custom_user'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='custom_users_permissions',
        related_query_name='custom_user_permission'
    )

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()

class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
class MyModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name