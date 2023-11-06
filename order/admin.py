from django.contrib import admin

from .models import Order,ClearedPickUps, ItemsPickedUp,ItemsDroppedOff,QualifiedForBonuses,AssignDriverToOrder,DriversCurrentLocation,ItemsInTransit,PendingOrders,ProcessingOrders


admin.site.register(Order)
admin.site.register(ClearedPickUps)
admin.site.register(ItemsPickedUp)
admin.site.register(ItemsDroppedOff)
admin.site.register(QualifiedForBonuses)
admin.site.register(AssignDriverToOrder)
admin.site.register(DriversCurrentLocation)
admin.site.register(ItemsInTransit)
admin.site.register(PendingOrders)
admin.site.register(ProcessingOrders)
