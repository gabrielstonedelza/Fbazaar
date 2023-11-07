from django.db import models
from orders.models import OrderItem
from cart.models import Cart
from users.models import User
from store_api.models import StoreItem

class Ordered(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(StoreItem,related_name="item_being_ordered",on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    unique_order_code = models.CharField(max_length=255, default="",blank=True)

    def __str__(self):
        return self.user.username

    def get_username(self):
        return self.user.username

    def get_item_name(self):
        return self.item.name

    def get_item_size(self):
        return self.item.size

    def get_item_pic(self):
        if self.item.picture:
            return "https://f-bazaar.com" + self.item.picture.url
        return ''

    def get_item_price(self):
        return self.item.old_price
