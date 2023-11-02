from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OrderItem
from users.models import User
from notifications.models import Notifications
from .sendemail import send_my_mail
from django.conf import settings
from django.core.mail import EmailMessage
from store_api.models import StoreItem


@receiver(post_save, sender=OrderItem)
def alert_order(sender, created, instance, **kwargs):
    title = f"New Order"
    message = f"{instance.user.username} has placed a new order"
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(item_id=instance.id,
                                     notification_title=title, notification_message=message,
                                     notification_from=instance.user, notification_to=admin_user,
                                     )
        # send_my_mail(f"New Order", settings.EMAIL_HOST_USER, settings.EMAIL_HOST_USER, {"item_name": instance.cart.item.name, "quantity": instance.quantity,"username":instance.user.username},
        #              "email_templates/order_email.html")

