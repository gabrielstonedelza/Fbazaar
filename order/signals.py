from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, ClearedPickUps, ItemsPickedUp,ItemsDroppedOff,QualifiedForBonuses,AssignDriverToOrder,DriversCurrentLocation,ItemsInTransit

from users.models import User
from notifications.models import Notifications
from .sendemail import send_my_mail
from django.conf import settings
from django.core.mail import EmailMessage
from store_api.models import StoreItem



@receiver(post_save,sender=DriversCurrentLocation)
def alert_driver_to_user_location(sender, created, instance, **kwargs):
    title = f"Driver is on the way"
    message = f"Hi {instance.user.username},driver {instance.driver.username} has picked up your order and is heading your way.You can track this order by going to your orders"
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(item_id=instance.id,
                                     notification_title=title, notification_message=message,
                                     notification_from=admin_user, notification_to=instance.order.user,
                                     )

@receiver(post_save,sender=AssignDriverToOrder)
def alert_driver_assigned_to_order(sender, created, instance, **kwargs):
    title = f"New Assigned Order"
    message = f"Hi {instance.driver.username},you have been assigned to order"
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(item_id=instance.id,
                                     notification_title=title, notification_message=message,
                                     notification_from=admin_user, notification_to=instance.driver,
                                     )


@receiver(post_save, sender=Order)
def alert_order(sender, created, instance, **kwargs):
    title = f"New Order"
    message = f"{instance.user.username} just placed a new order"
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(item_id=instance.id,
                                     notification_title=title, notification_message=message,
                                     notification_from=instance.user, notification_to=admin_user,
                                     )
        send_my_mail(f"New Order", settings.EMAIL_HOST_USER, settings.EMAIL_HOST_USER, {"item_name": instance.unique_order_code, "username":instance.user.username},
                     "email_templates/order_email.html")


@receiver(post_save, sender=ClearedPickUps)
def alert_order_cleared_for_pickup(sender, created, instance, **kwargs):
    title = f"Order cleared"
    message_to_wear_house = f"Order has been cleared for processing and pickup"
    message_to_customer = f"Your order has been cleared for processing and pickup"
    admin_user = User.objects.get(id=1)
    wear_house_manager = User.objects.get(username="wholesale")
    user_ordering = User.objects.get(username=instance.order.user.username)

    if created:
        Notifications.objects.create(item_id=instance.id,
                                     notification_title=title, notification_message=message_to_wear_house,
                                     notification_from=admin_user, notification_to=wear_house_manager,
                                     )
        Notifications.objects.create(item_id=instance.id,
                                     notification_title=title, notification_message=message_to_customer,
                                     notification_from=admin_user, notification_to=instance.order.user,
                                     )
        send_my_mail(f"Item Cleared", settings.EMAIL_HOST_USER, user_ordering.email,
                     {"item_name": instance.order.unique_order_code,
                      "username": instance.order.user.username,},
                     "email_templates/cleared_for_pickup_email.html")

@receiver(post_save, sender=ItemsPickedUp)
def alert_order_picked_up(sender, created, instance, **kwargs):
    title = f"Order Picked up"
    message_to_admin = f"Order has been picked up and on the way to the customer"
    message_to_customer = f"Your order has been picked up and on the way"
    admin_user = User.objects.get(id=1)
    user_ordering = User.objects.get(username=instance.order.user.username)

    if created:
        Notifications.objects.create(item_id=instance.id,
                                     notification_title=title, notification_message=message_to_admin,
                                     notification_from=instance.user, notification_to=admin_user,
                                     )
        Notifications.objects.create(item_id=instance.id,
                                     notification_title=title, notification_message=message_to_customer,
                                     notification_from=instance.user, notification_to=instance.order.user,
                                     )

        send_my_mail(f"Order Picked up", settings.EMAIL_HOST_USER, user_ordering.email,
                     {"item_name": instance.order.unique_order_code,
                      "username": instance.order.user.username,},
                     "email_templates/order_picked_up_email.html")

@receiver(post_save, sender=ItemsInTransit)
def alert_order_in_transit(sender, created, instance, **kwargs):
    title = f"Order in transit"
    message = f"Order has been picked up and on the way"
    user_ordering = User.objects.get(username=instance.order.user.username)

    if created:
        Notifications.objects.create(item_id=instance.id,
                                     notification_title=title, notification_message=message,
                                     notification_from=instance.driver, notification_to=instance.order.user,
                                     )
@receiver(post_save, sender=ItemsDroppedOff)
def alert_order_dropped_off(sender, created, instance, **kwargs):
    title = f"Order Delivered"
    message_to_admin = f"Order has been delivered to the customers location"
    message_to_customer = f"Your order has been delivered to your location"
    admin_user = User.objects.get(id=1)
    user_ordering = User.objects.get(username=instance.order.user.username)

    if created:
        Notifications.objects.create(item_id=instance.id,
                                     notification_title=title, notification_message=message_to_admin,
                                     notification_from=instance.user, notification_to=admin_user,
                                     )

        Notifications.objects.create(item_id=instance.id,
                                     notification_title=title, notification_message=message_to_customer,
                                     notification_from=instance.user, notification_to=instance.order.user,
                                     )

        send_my_mail(f"Order Delivered", settings.EMAIL_HOST_USER, user_ordering.email,
                     {"item_name": instance.order.unique_order_code,
                      "username": instance.order.user.username,},
                     "email_templates/order_dropped_off_email.html")

        send_my_mail(f"Order Delivered", settings.EMAIL_HOST_USER, admin_user.email,
                     {"item_name": instance.order.unique_order_code,
                      "username": instance.order.user.username, },
                     "email_templates/order_dropped_off_email_for_admin.html")

@receiver(post_save, sender=QualifiedForBonuses)
def alert_qualified_for_bonus(sender, created, instance, **kwargs):
    title = f"Bonus Qualification"
    message = f"Hi,{instance.user.username} you have qualified for bonus on any item you purchase"
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(item_id=instance.id,
                                     notification_title=title, notification_message=message,
                                     notification_from=admin_user, notification_to=instance.user,
                                     )