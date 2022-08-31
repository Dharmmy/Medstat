from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models
# Create your models here.




class AccountManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must have is_staff=True."
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must have is_superuser=True."
            )

        return self._create_user(email, password, **extra_fields)


class Account(AbstractBaseUser,PermissionsMixin):
    email         = models.EmailField(_('email address'),max_length=60,unique=True)
    username      = models.CharField(max_length=30,unique=True)
    hospital_name    = models.CharField(max_length=60,blank=True)
    unit_name     = models.CharField(max_length=60,blank=True)
    local_government  = models.CharField(max_length=100,blank=True)
    state  = models.CharField(max_length=100,blank=True)
    date_joined   = models.DateTimeField(verbose_name='date_joined',auto_now_add=True)
    last_login    = models.DateTimeField(verbose_name='last login',auto_now=True)
    is_admin      = models.BooleanField(default=False)
    is_active     = models.BooleanField(default=True)
    is_staff      = models.BooleanField(default=False)
    is_superuser  = models.BooleanField(default=False)


    def __str__(self):
        return f' {self.username}, {self.email}, {self.hospital_name}, {self.unit_name}, {self.local_government}, {self.state}'


    objects = AccountManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','hospital_name', 'unit_name', 'local_government', 'state']

    