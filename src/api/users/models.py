import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken

class MyAccountManager(BaseUserManager):
    def create_user(self, email=None, password=None, date_of_birth=None, profile_image=None, name=None, **extra_fields):
        extra_fields.setdefault('is_admin', False)
        extra_fields.setdefault('is_active', True)
        
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')

        email = self.normalize_email(email)
        user = self.model(email=email, date_of_birth=date_of_birth, profile_image=profile_image, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, date_of_birth=None, profile_image=None, name=None, **extra_fields):
        user = self.create_user(
            email=email,
            password=password,
            date_of_birth=date_of_birth,
            profile_image=profile_image,
            name=name,
            is_active=True
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    date_of_birth = models.DateTimeField(default=datetime.date.today)
    profile_image = models.CharField(max_length=128, default='https://st.depositphotos.com/1779253/5140/v/380/depositphotos_51405259-stock-illustration-male-avatar-profile-picture-use.jpg', null=True, blank=True)
    name = models.CharField(max_length=128, default='', null=True, blank=True)
    #### Removed fields ####
    last_login = None      #
    username = None        #
    is_superuser = None    #
    ########################
    
    USERNAME_FIELD = 'email'

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def token(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
    class Meta:
        db_table = "users"