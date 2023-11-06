from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.models import Notifications

from users.models import User
from .models import StoreItem,AddToPriceChanged,ItemRatings,ItemRemarks, NotifyAboutItemVerified,NotifyAboutItemRejected

@receiver(post_save, sender=NotifyAboutItemVerified)
def alert_verified_item(sender, created, instance, **kwargs):
    title = f"Item Verified"
    message = f"Hi, your item with the name {instance.item.name} was verified"
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(item_id=instance.id,
                                 notification_title=title, notification_message=message,
                                 notification_from=admin_user, notification_to=instance.user,
                                 )

@receiver(post_save, sender=NotifyAboutItemRejected)
def alert_rejected_item(sender, created, instance, **kwargs):
    title = f"Item Rejected"
    message = f"Hi, your item with the name {instance.item.name} was rejected because it did not meet the requirements."
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(item_id=instance.id,
                                 notification_title=title, notification_message=message,
                                 notification_from=admin_user, notification_to=instance.user,
                                 )

@receiver(post_save, sender=StoreItem)
def alert_new_item(sender, created, instance, **kwargs):
    title = f"New Item"
    message = f"Hi, FBazaar added new item to their list"
    admin_user = User.objects.get(id=1)
    users = User.objects.exclude(id=1)

    if created:
        for i in users:
            Notifications.objects.create(item_id=instance.id,
                                     notification_title=title, notification_message=message,
                                     notification_from=admin_user, notification_to=i,
                                     )

@receiver(post_save, sender=AddToPriceChanged)
def alert_item_price_update(sender, created, instance, **kwargs):
    title = f"Item Updated"
    message = f"Hi,{instance.user.username}, FBazaar updated the price of {instance.ordered_item.name},login and check it out"
    admin_user = User.objects.get(id=1)
    users = User.objects.exclude(id=1)

    if created:
        for i in users:
            Notifications.objects.create(item_id=instance.id,
                                     notification_title=title, notification_message=message,
                                     notification_from=admin_user, notification_to=i,
                                     )