from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,UserManager,PermissionsMixin,BaseUserManager
from django.conf import settings

DeUser = settings.AUTH_USER_MODEL

USER_TYPES = (
    ("Administrator", "Administrator"),
    ("Customer", "Customer"),
    ("Driver", "Driver"),
    ("Warehouse Manager", "Warehouse Manager"),
    ("Stock Manager", "Stock Manager"),
)

# class CustomUserManager(UserManager):
#     def _create_user(self, email,password,**extra_fields):
#         if not email:
#             raise ValueError("Please provide a valid email address")
#
#         email = self.normalize_email(email)
#         user = self.model(email=email,**extra_fields)
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_user(self, email=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)
#
#     def create_superuser(self, email=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self._create_user(email, password, **extra_fields)
#
# class User(AbstractBaseUser,PermissionsMixin):
#     email = models.EmailField(unique=True, max_length=255)
#     phone = models.CharField(max_length=15, unique=True)
#     user_type = models.CharField(max_length=80,choices=USER_TYPES,default="Customer")
#     name = models.CharField(max_length=100, unique=True)
#     company_name = models.CharField(max_length=100, unique=True,blank=True,default="")
#     user_blocked = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     last_login = models.DateTimeField(auto_now_add=True,null=True,blank=True)
#
#     objects = CustomUserManager()
#
#
#     # REQUIRED_FIELDS = ['username', 'phone','user_type','name','company_name']
#     REQUIRED_FIELDS = []
#     USERNAME_FIELD = 'email'
#
#     class Meta:
#         verbose_name = "User"
#         verbose_name_plural = "Users"
#
#     def get_full_name(self):
#         return self.name
#
#     def get_short_name(self):
#         return self.name or self.email.split("@")[0]



class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    phone = models.CharField(max_length=15, unique=True)
    user_type = models.CharField(max_length=80,choices=USER_TYPES,default="Customer")
    name = models.CharField(max_length=100, unique=True)
    store = models.CharField(max_length=100, unique=True, default="FBazaar",blank=True)
    store_location = models.CharField(max_length=100,default="Airport Round About",blank=True)
    user_blocked = models.BooleanField(default=False)


    REQUIRED_FIELDS = ['username','phone','user_type','name','store','store_location']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.username
#

