from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OrderItem, ClearedPickUps, ItemsPickedUp,ItemsDroppedOff,QualifiedForBonuses
from users.models import User
from notifications.models import Notifications
from .sendemail import send_my_mail
from django.conf import settings
from django.core.mail import EmailMessage
from store_api.models import StoreItem


@receiver(post_save, sender=OrderItem)
def alert_order(sender, created, instance, **kwargs):
    title = f"New Order"
    message = f"{instance.user.username} is ordering {instance.quantity} of {instance.item.name}"
    admin_user = User.objects.get(id=1)
    # image_instance = StoreItem.objects.filter(size=instance.size)[:1] # Replace 'image_id' with the actual ID of the image you want to send.
    # image_data = image_instance.picture.read()

    if created:
        Notifications.objects.create(item_id=instance.id,
                                     notification_title=title, notification_message=message,
                                     notification_from=instance.user, notification_to=admin_user,
                                     )
        send_my_mail(f"New Order", settings.EMAIL_HOST_USER, settings.EMAIL_HOST_USER, {"item_name": instance.item.name, "quantity": instance.quantity,"username":instance.user.username},
                     "email_templates/order_email.html")
        # email = EmailMessage(
        #     'New Order',
        #     f'{instance.user.username} want to purchase {instance.quantity} boxes of {instance.item.name}',
        #     settings.EMAIL_HOST_USER,  # Replace with the sender's email address
        #     [settings.EMAIL_HOST_USER],  # Replace with the recipient's email address
        # )
        #
        # # Attach the image to the email
        # email.attach(f'{instance.item.name}.jpg', image_data,
        #              'image/jpeg')  # You can change the filename and content type as needed

        # Send the email
        # email.send()



@receiver(post_save, sender=ClearedPickUps)
def alert_order_cleared_for_pickup(sender, created, instance, **kwargs):
    title = f"Order cleared"
    message = f"{instance.order_item.pk} has been cleared for pickup"
    admin_user = User.objects.get(id=1)
    wear_house_manager = User.objects.get(user_type="Warehouse Manager")
    user_ordering = User.objects.get(username=instance.order_item.user.username)

    if created:
        Notifications.objects.create(item_id=instance.id,
                                     notification_title=title, notification_message=message,
                                     notification_from=admin_user, notification_to=wear_house_manager,
                                     )
        send_my_mail(f"Item Cleared", settings.EMAIL_HOST_USER, user_ordering.email,
                     {"item_name": instance.order_item.item.name,
                      "username": instance.order_item.user.username,"quantity":instance.order_item.quantity},
                     "email_templates/cleared_for_pickup_email.html")

@receiver(post_save, sender=ItemsPickedUp)
def alert_order_picked_up(sender, created, instance, **kwargs):
    title = f"Order Picked up"
    message = f"{instance.order_item.pk} has been picked up and on the way"
    admin_user = User.objects.get(id=1)
    user_ordering = User.objects.get(username=instance.order_item.user.username)

    if created:
        Notifications.objects.create(item_id=instance.id,
                                     notification_title=title, notification_message=message,
                                     notification_from=instance.user, notification_to=admin_user,
                                     )

        send_my_mail(f"Order Picked up", settings.EMAIL_HOST_USER, user_ordering.email,
                     {"item_name": instance.order_item.item.name,
                      "username": instance.order_item.user.username, "quantity": instance.order_item.quantity},
                     "email_templates/order_picked_up_email.html")


@receiver(post_save, sender=ItemsDroppedOff)
def alert_order_dropped_off(sender, created, instance, **kwargs):
    title = f"Order Delivered"
    message = f"{instance.order_item.pk} has been delivered to the customers location"
    admin_user = User.objects.get(id=1)
    user_ordering = User.objects.get(username=instance.order_item.user.username)

    if created:
        Notifications.objects.create(item_id=instance.id,
                                     notification_title=title, notification_message=message,
                                     notification_from=instance.user, notification_to=admin_user,
                                     )

        send_my_mail(f"Order Delivered", settings.EMAIL_HOST_USER, user_ordering.email,
                     {"item_name": instance.order_item.item.name,
                      "username": instance.order_item.user.username, "quantity": instance.order_item.quantity},
                     "email_templates/order_dropped_off_email.html")

        send_my_mail(f"Order Delivered", settings.EMAIL_HOST_USER, admin_user.email,
                     {"item_name": instance.order_item.item.name,
                      "username": instance.order_item.user.username, "quantity": instance.order_item.quantity},
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