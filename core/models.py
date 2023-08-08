from django.db import models  # noqa
from django.utils import timezone
from django.conf import settings

# Create your models here.


from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users"""

    def create_user(self, email: str, password: str = None, **extra_fields):

        if not email:
            raise ValueError("Email field can NOT be blank")

        if len(password) < 5:
            raise ValueError("Password is too short")


        user = self.model(email=self.normalize_email(email), **extra_fields)

        user.set_password(password)

        # it is best practice to pass `using=self._db`
        # when we are using multiple databases
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in application"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = "email"  # overrides the default user field from base class


class Post(models.Model):
    auther = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=250, unique=True)
    body = models.TextField()

    def __str__(self):
        return self.title


