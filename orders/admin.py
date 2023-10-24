from django.contrib import admin

from .models import OrderItem, ClearedPickUps, ItemsPickedUp,ItemsDroppedOff,QualifiedForBonuses,AssignDriverToOrder,DriversCurrentLocation,ItemsInTransit

admin.site.register(ItemsInTransit)
admin.site.register(DriversCurrentLocation)
admin.site.register(AssignDriverToOrder)
admin.site.register(QualifiedForBonuses)
admin.site.register(OrderItem)
admin.site.register(ClearedPickUps)
admin.site.register(ItemsPickedUp)
admin.site.register(ItemsDroppedOff)
