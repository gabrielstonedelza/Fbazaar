from django.db import models
from PIL import Image
from users.models import User
from profiles.models import Profile

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

class StoreItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    store = models.CharField(max_length=255,blank=True)
    name = models.CharField(max_length=255,blank=True)
    category = models.CharField(max_length=80, default="Water",choices=ITEM_CATEGORIES,blank=True)
    size = models.CharField(max_length=30, choices=ITEM_SIZE, default="Small",blank=True)
    old_price = models.DecimalField(max_digits=19, decimal_places=2, blank=True,default=0.0)
    new_price = models.DecimalField(max_digits=19, decimal_places=2, blank=True,default=0.0)
    retail_price = models.DecimalField(max_digits=19, decimal_places=2, blank=True,default=0.0)
    wholesale_price = models.DecimalField(max_digits=19, decimal_places=2, blank=True,default=0.0)
    picture = models.ImageField(upload_to="store_items",blank=True)
    volume = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    exclusive = models.BooleanField(default=False)
    promotion = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    quantity_qualify_for_free_delivery = models.IntegerField(default=20)
    quantity_needed_for_wholesale_price = models.IntegerField(default=20)
    item_verified = models.BooleanField(default=False)
    item_rejected = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.picture.path)

    def get_item_pic(self):
        if self.picture:
            return "https://f-bazaar.com" + self.picture.url
        return ''


class AddToPriceChanged(models.Model):
    item = models.ForeignKey(StoreItem,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item.name}'s price has changed"

class ItemRatings(models.Model):
    item = models.ForeignKey(StoreItem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_rating")
    rating = models.IntegerField(default=0)
    date_rated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.rating)


class ItemRemarks(models.Model):
    item = models.ForeignKey(StoreItem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_making_remarks")
    remark = models.TextField()
    rating = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} gave a remark "

    def get_username(self):
        return self.user.username

    def get_profile_pic(self):
        de_user = Profile.objects.get(user=self.user)
        if de_user:
            return "https://f-bazaar.com" + de_user.profile_pic.url
        return ''


class NotifyAboutItemVerified(models.Model):
    item = models.ForeignKey(StoreItem, on_delete=models.CASCADE,related_name="item_to_verify",)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_verified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item.name


class NotifyAboutItemRejected(models.Model):
    item = models.ForeignKey(StoreItem, on_delete=models.CASCADE, related_name="item_to_reject", )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_rejected = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item.name