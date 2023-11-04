from django.db import models
from django.conf import settings
from PIL import Image

DeUser = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.OneToOneField(DeUser, on_delete=models.CASCADE, related_name="profile_user")
    profile_pic = models.ImageField(upload_to="profile_pics", default="default_user.png")

    def __str__(self):
        return self.user.name

    def get_user_type(self):
        return self.user.user_type

    def get_phone(self):
        return self.user.phone

    def get_email(self):
        return self.user.email

    def get_username(self):
        return self.user.username

    def get_users_fullname(self):
        return self.user.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

    def get_profile_pic(self):
        if self.profile_pic:
            return "https://f-bazaar.com" + self.profile_pic.url
        return ''
