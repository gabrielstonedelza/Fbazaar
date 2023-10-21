from django.db import models
from users.models import User
from store_api.models import StoreItem

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(StoreItem,on_delete=models.CASCADE,related_name="item")
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=19, decimal_places=2, blank=True, default=0.0)
    date_added = models.DateTimeField(auto_now_add=True)

    def get_item_name(self):
        return self.item.name

    def get_username(self):
        return self.user.username


    def get_item_price(self):
        return self.item.new_price

    def get_item_size(self):
        return self.item.size

    def get_item_pic(self):
        if self.item.picture:
            return "https://f-bazaar.com" + self.item.picture.url
        return ''

    def get_item_category(self):
        return self.item.category


    def __str__(self):
        return self.item.name

