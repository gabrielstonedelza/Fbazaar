from django.db import models
from users.models import User
from store_api.models import StoreItem
from orders.models import OrderItem


PAYMENT_METHODS=(
    ("Payment Before Delivery","Payment Before Delivery"),
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
    ("Not Processed","Not Processed"),
    ("Pending","Pending"),
    ("Processing","Processing"),
    ("Picked Up","Picked Up"),
    ("In Transit","In Transit"),
    ("Delivered","Delivered"),
)

DELIVERY_METHOD = (
    ("Taxinet Delivery","Taxinet Delivery"),
    ("Delivery","Delivery"),
    ("Pick Up","Pick Up"),
)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem,related_name="orders", blank=True)
    payment_method = models.CharField(max_length=80, default="Cash On Delivery", choices=PAYMENT_METHODS)
    drop_off_location_lat = models.CharField(max_length=255, blank=True)
    drop_off_location_lng = models.CharField(max_length=255, blank=True)
    date_order_created = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=70, choices=ORDER_STATUS, default="Not Processed")
    delivery_method = models.CharField(max_length=50, default="Delivery")
    order_total_price = models.DecimalField(max_digits=19, decimal_places=2,default=0.0)
    delivered = models.BooleanField(default=False)
    ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    unique_order_code = models.CharField(max_length=255, default="",blank=True)

    def __str__(self):
        return self.user.username


class ClearedPickUps(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order.pk} has been cleared for pickup"


class AssignDriverToOrder(models.Model):
    user_with_order =  models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name="order_being_assigned")
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assigned_driver")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.driver.username} has been assigned to order {self.order.items.name}"

    def get_item_code(self):
        return self.order.unique_order_code


    def get_ordered_username(self):
        return self.order.user.username


class ItemsPickedUp(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wear_house_manager")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order.pk} has been picked up by driver"

    def get_username(self):
        return self.user.username

class PendingOrders(models.Model):
    user_with_order = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name="status_pending")
    order_status = models.CharField(max_length=70, choices=ORDER_STATUS, default="Not Processed")
    pass_pending = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order.unique_order_code

    def get_ordered_username(self):
        return self.order.user.username

    def get_order_code(self):
        return self.order.unique_order_code

    def get_items(self):
        all_items_names = []
        all_items_sizes = []
        all_items_pictures = []
        all_items_prices = []

        for i in self.order.items.all():
            all_items_names.append(i.item.name)
            all_items_sizes.append(i.item.size)
            all_items_prices.append(i.item.old_price)
            if i.item.picture:
                item_pic = "https://f-bazaar.com" + i.item.picture.url
                all_items_pictures.append(item_pic)
        return all_items_names,all_items_sizes,all_items_pictures,all_items_prices

class ProcessingOrders(models.Model):
    user_with_order = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name="status_processing")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_updating_processing")
    order_status = models.CharField(max_length=70, choices=ORDER_STATUS, default="Not Processed")
    pass_processing = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_ordered_username(self):
        return self.order.user.username

    def get_order_code(self):
        return self.order.unique_order_code

class ItemsInTransit(models.Model):
    user_with_order = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name="status_in_transit")
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="driver_sending_order")
    order_status = models.CharField(max_length=70, choices=ORDER_STATUS, default="Not Processed")
    pass_in_transit = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order.pk} has been picked up by driver"

    def get_username(self):
        return self.user.username

    def get_ordered_username(self):
        return self.order.user.username

    def get_order_code(self):
        return self.order.unique_order_code


class ItemsDroppedOff(models.Model):
    user_with_order = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name="status_delivered")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="driver")
    order_status = models.CharField(max_length=70, choices=ORDER_STATUS, default="Not Processed")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order.pk} has been dropped off {self.order.user.username}'s location by driver"


    def get_ordered_username(self):
        return self.order.user.username

    def get_order_code(self):
        return self.order.unique_order_code


class QualifiedForBonuses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} has qualified for bonus"


class DriversCurrentLocation(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="ordered_item")
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_receiving_order")
    drivers_lat = models.CharField(max_length=255)
    drivers_lng = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order.ordered_item.name

    def get_drivers_name(self):
        return self.driver.username

    def get_order_user(self):
        return self.user.username

