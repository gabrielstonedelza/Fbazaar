from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

DeUser = settings.AUTH_USER_MODEL

USER_TYPES = (
    ("Administrator", "Administrator"),
    ("Customer", "Customer"),
    ("Driver", "Driver"),
    ("Warehouse Manager", "Warehouse Manager"),
)

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    phone = models.CharField(max_length=15, unique=True, help_text="please format should be +233")
    user_type = models.CharField(max_length=80,choices=USER_TYPES,default="Customer")
    full_name = models.CharField(max_length=100, unique=True, default="")
    user_blocked = models.BooleanField(default=False)
    agreed_to_supplied = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['username', 'phone','user_type','full_name']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.username

