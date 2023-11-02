from django.db import models
from users.models import User
from store_api.models import StoreItem


class OrderItem(models.Model):
    item = models.ForeignKey(StoreItem,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_purchasing")
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def get_item_total_price(self):
        return self.quantity * self.item.old_price

    # def save(self, *args, **kwargs):
    #     total_price = float(self.price) * float(self.quantity)
    #     self.price = total_price
    #     super().save(*args, **kwargs)

    def get_store_name(self):
        return self.item.company_name

    def __str__(self):
        return self.item.name

    def get_item_name(self):
        return self.item.name

    def get_username(self):
        return self.user.username

    def get_item_pic(self):
        if self.item.picture:
            return "https://f-bazaar.com" + self.item.picture.url
        return ''

    def get_item_size(self):
        return self.item.size

    def get_item_price(self):
        return self.item.old_price

