from django.db import models
from users.models import User

from store_api.models import StoreItem
from cart.models import Cart

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

ORDER_STATUS = (
    ("Pending","Pending"),
    ("Processing","Processing"),
    ("Picked Up","Picked Up"),
    ("In Transit","In Transit"),
    ("Delivered","Delivered"),
)

DELIVERY_METHOD = (
    ("Delivery","Delivery"),
    ("Pick Up","Pick Up"),
)

class OrderItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_purchasing")
    quantity = models.IntegerField(default=0)
    category = models.CharField(max_length=80, default="Water", choices=ITEM_CATEGORIES)
    size = models.CharField(max_length=30, choices=ITEM_SIZE, default="Small")
    price = models.DecimalField(max_digits=19, decimal_places=2, blank=True)
    payment_method = models.CharField(max_length=80, default="Cash On Delivery", choices=PAYMENT_METHODS)
    drop_off_location_lat = models.CharField(max_length=255,blank=True)
    drop_off_location_lng = models.CharField(max_length=255,blank=True)
    date_order_created = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=70,choices=ORDER_STATUS,default="Pending")
    delivery_method = models.CharField(max_length=50,default="Delivery")
    ordered = models.BooleanField(default=False)
    unique_order_code = models.CharField(max_length=255,default="")

    def save(self, *args, **kwargs):
        total_price = float(self.price) * float(self.quantity)
        self.price = total_price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.cart.item.name

    def get_item_name(self):
        return self.cart.item.name

    def get_username(self):
        return self.user.username

    def get_item_pic(self):
        if self.cart.item.picture:
            return "https://f-bazaar.com" + self.cart.item.picture.url
        return ''

    def get_item_size(self):
        return self.cart.item.size

    def get_item_price(self):
        return self.cart.price


class ClearedPickUps(models.Model):
    order_item = models.ForeignKey(OrderItem,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order_item.pk} has been cleared for pickup"

class AssignDriverToOrder(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assigned_driver")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.driver.username} has been assigned to order {self.order_item.cart.item.name}"

    def get_item_name(self):
        return self.order_item.cart.item.name

    def get_item_size(self):
        return self.order_item.cart.item.size

    def get_item_pic(self):
        if self.order_item.cart.item.picture:
            return "https://f-bazaar.com" + self.order_item.cart.item.picture.url
        return ''

    def get_ordered_username(self):
        return self.order_item.user.username

    def get_order_quantity(self):
        return self.order_item.quantity

    def get_order_status(self):
        return self.order_item.order_status
    def get_item_price(self):
        return self.order_item.price

class ItemsPickedUp(models.Model):
    order_item = models.ForeignKey(OrderItem,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wear_house_manager")
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.order_item.pk} has been picked up by driver"


    def get_username(self):
        return self.user.username

class ItemsInTransit(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="driver_sending_order")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order_item.pk} has been picked up by driver"

    def get_username(self):
        return self.user.username


class ItemsDroppedOff(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="driver")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order_item.pk} has been dropped off {self.order_item.user.username}'s location by driver"

    def get_item_name(self):
        return self.order_item.cart.item.name

    def get_item_size(self):
        return self.order_item.cart.item.size

    def get_item_pic(self):
        if self.order_item.cart.item.picture:
            return "https://f-bazaar.com" + self.order_item.cart.item.picture.url
        return ''

    def get_ordered_username(self):
        return self.order_item.user.username

    def get_order_quantity(self):
        return self.order_item.quantity

    def get_order_status(self):
        return self.order_item.order_status
    def get_item_price(self):
        return self.order_item.price
    

class QualifiedForBonuses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} has qualified for bonus"


class DriversCurrentLocation(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name="ordered_item")
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_receiving_order")
    drivers_lat = models.CharField(max_length=255)
    drivers_lng = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.order_item.cart.item.name

    def get_drivers_name(self):
        return self.driver.username

    def get_order_user(self):
        return self.user.username