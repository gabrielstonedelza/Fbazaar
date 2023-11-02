from django.db import models
from users.models import User
from store_api.models import StoreItem
from orders.models import OrderItem

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ordered_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name="ordering_item",blank=True,null=True)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=19, decimal_places=2, blank=True, default=0.0)
    date_added = models.DateTimeField(auto_now_add=True)

    def get_item_name(self):
        return self.ordered_item.name

    def get_username(self):
        return self.user.username


    def get_item_price(self):
        return self.ordered_item.new_price

    def get_item_size(self):
        return self.ordered_item.size

    def get_item_pic(self):
        if self.ordered_item.picture:
            return "https://f-bazaar.com" + self.ordered_item.picture.url
        return ''

    def get_item_category(self):
        return self.ordered_item.category


    def __str__(self):
        return self.ordered_item.name

