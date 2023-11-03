from django.db import models
from orders.models import OrderItem
from cart.models import Cart
from users.models import User

class Ordered(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Cart,related_name="items_being_ordered")
    ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
