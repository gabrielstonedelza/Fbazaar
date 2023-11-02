from django.db import models
from users.models import User
from store_api.models import StoreItem


# ITEM_CATEGORIES = (
#     ("Water","Water"),
#     ("Drinks","Drinks"),
# )
#
# ITEM_SIZE =(
#     ("Small","Small"),
#     ("Medium","Medium"),
#     ("Large","Large"),
#     ("Extra Large","Extra Large"),
# )
#
# PAYMENT_METHODS=(
#     ("Payment Before Delivery","Payment Before Delivery"),
#     ("Cash On Delivery","Cash On Delivery"),
# )
#
# PICK_UP_STATUS=(
#     ("Cleared for pickup","Cleared for pickup"),
#     ("Not cleared for pickup","Not cleared for pickup"),
# )
#
# PICKED_UP_STATUS=(
#     ("Items Picked","Items Picked"),
#     ("Items not picked up yet","Items not picked up yet"),
# )
#
# ORDER_STATUS = (
#     ("Pending","Pending"),
#     ("Processing","Processing"),
#     ("Picked Up","Picked Up"),
#     ("In Transit","In Transit"),
#     ("Delivered","Delivered"),
# )
#
# DELIVERY_METHOD = (
#     ("Taxinet Delivery","Taxinet Delivery"),
#     ("Delivery","Delivery"),
#     ("Pick Up","Pick Up"),
# )


class OrderItem(models.Model):
    item = models.ForeignKey(StoreItem,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_purchasing")
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def get_item_total_price(self):
        return self.quantity * self.item.new_price

    # def save(self, *args, **kwargs):
    #     total_price = float(self.price) * float(self.quantity)
    #     self.price = total_price
    #     super().save(*args, **kwargs)

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
        return self.item.new_price

