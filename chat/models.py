from django.db import models
from users.models import User

ROOM_STATUS = (
    ("Waiting","Waiting"),
    ("Active","Active"),
    ("Closed","Closed"),
)


class Message(models.Model):
    body = models.TextField()
    sent_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, blank=True, null=True,on_delete=models.SET_NULL)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"{self.sent_by}"

class Room(models.Model):
    uuid = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    agent = models.ForeignKey(User, blank=True, null=True,related_name='rooms',on_delete=models.SET_NULL)
    messages = models.ManyToManyField(Message,blank=True)
    url = models.CharField(max_length=255,blank=True,null=True)
    status = models.CharField(max_length=20, choices=ROOM_STATUS,default="Waiting")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.client}"