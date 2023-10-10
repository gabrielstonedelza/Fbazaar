from django.db import models
from users.models import User

from store_api.models import StoreItem

ITEM_CATEGORIES = (
    ("Water","Water"),
    ("Drinks","Drinks"),
)

ITEM_SIZE =(
    ("Small","Small"),
    ("Medium","Medium"),
    ("Large","Large"),
    ("Extra Large","Extra Large"),
)

PAYMENT_METHODS=(
    ("Mobile Money","Mobile Money"),
    ("Cash On Delivery","Cash On Delivery"),
)

PICK_UP_STATUS=(
    ("Cleared for pickup","Cleared for pickup"),
    ("Not cleared for pickup","Not cleared for pickup"),
)

PICKED_UP_STATUS=(
    ("Items Picked","Items Picked"),
    ("Items not picked up yet","Items not picked up yet"),
)

class OrderItem(models.Model):
    item = models.ForeignKey(StoreItem,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_purchasing")
    quantity = models.IntegerField(default=0)
    category = models.CharField(max_length=80, default="Water", choices=ITEM_CATEGORIES)
    size = models.CharField(max_length=30, choices=ITEM_SIZE, default="Small")
    price = models.DecimalField(max_digits=19, decimal_places=2, blank=True)
    payment_method = models.CharField(max_length=80, default="Cash On Delivery", choices=PAYMENT_METHODS)
    drop_off_location = models.CharField(max_length=255,blank=True)
    date_order_created = models.DateTimeField(auto_now_add=True)
    order_pick_up_status = models.CharField(max_length=50,default="Not cleared for pickup", choices=PICK_UP_STATUS)
    order_picked_up_status = models.CharField(max_length=50,default="Items not picked up yet", choices=PICKED_UP_STATUS)
    item_dropped_off = models.BooleanField(default=False)
    ordered = models.BooleanField(default=False)

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

class ClearedPickUps(models.Model):
    order_item = models.ForeignKey(OrderItem,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order_item.pk} has been cleared for pickup"


class ItemsPickedUp(models.Model):
    order_item = models.ForeignKey(OrderItem,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wear_house_manager")
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.order_item.pk} has been picked up by driver"


class ItemsDroppedOff(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="driver")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order_item.pk} has been dropped off {self.order_item.user.username}'s location by driver"
    

class QualifiedForBonuses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} has qualified for bonus"