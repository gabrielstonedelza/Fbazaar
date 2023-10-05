from django.contrib import admin

from .models import StoreItem,AddToPriceChanged,ItemRatings,ItemRemarks

admin.site.register(StoreItem)
admin.site.register(AddToPriceChanged)
admin.site.register(ItemRatings)
admin.site.register(ItemRemarks)
