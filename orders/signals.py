from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OrderItem, ClearedPickUps, ItemsPickedUp,ItemsDroppedOff,QualifiedForBonuses
from users.models import User
from notifications.models import Notifications


@receiver(post_save, sender=OrderItem)
def alert_order(sender, created, instance, **kwargs):
    title = f"New Order"
    message = f"{instance.user.username} is ordering {instance.item.quantity} of {instance.item.name}"
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(item_id=instance.id,
                                     notification_title=title, notification_message=message,
                                     notification_from=instance.user, notification_to=admin_user,
                                     )


@receiver(post_save, sender=ClearedPickUps)
def alert_order_cleared_for_pickup(sender, created, instance, **kwargs):
    title = f"Order cleared"
    message = f"{instance.order_item.pk} has been cleared for pickup"
    admin_user = User.objects.get(id=1)
    wear_house_manager = User.objects.get(user_type="Warehouse Manager")

    if created:
        Notifications.objects.create(item_id=instance.id,
                                     notification_title=title, notification_message=message,
                                     notification_from=admin_user, notification_to=wear_house_manager,
                                     )

@receiver(post_save, sender=ItemsPickedUp)
def alert_order_picked_up(sender, created, instance, **kwargs):
    title = f"Order Picked up"
    message = f"{instance.order_item.pk} has been picked up"
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(item_id=instance.id,
                                     notification_title=title, notification_message=message,
                                     notification_from=instance.user, notification_to=admin_user,
                                     )


@receiver(post_save, sender=ItemsDroppedOff)
def alert_order_dropped_off(sender, created, instance, **kwargs):
    title = f"Order Delivered"
    message = f"{instance.order_item.pk} has been delivered to the customers location"
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(item_id=instance.id,
                                     notification_title=title, notification_message=message,
                                     notification_from=instance.user, notification_to=admin_user,
                                     )

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