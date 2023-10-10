from django.db import models

from users.models import User
from store_api.models import StoreItem

class Favorites(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(StoreItem, on_delete=models.CASCADE,related_name='favorites')
    date_added = models.DateTimeField(auto_now_add=True)

    def get_item_name(self):
        return self.item.name

    def get_item_price(self):
        return self.item.new_price

    def get_item_pic(self):
        if self.item.picture:
            return "https://f-bazaar.com" + self.item.picture.url
        return ''


    def __str__(self):
        return self.item.name
