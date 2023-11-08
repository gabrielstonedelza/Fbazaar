from django.db import models
from users.models import User

class RegisterStore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=255,unique=True)
    location = models.CharField(max_length=255,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_username(self):
        return self.user.username

class StoreRatings(models.Model):
    store = models.ForeignKey(RegisterStore,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_rating_store")
    rating = models.IntegerField(default=0)
    date_rated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.rating)
