from django.urls import path
from . import views

urlpatterns =[
    path("place_order/<int:id>/",views.place_order),
    path("my_orders/",views.get_my_orders),
    path("clear_order/",views.add_to_cleared),
    path("cleared_orders/",views.get_cleared_for_pickup),
    path("picked_up_orders/",views.get_orders_picked_up),
    path("dropped_off_orders/",views.get_orders_dropped_off),
    path("add_to_picked_up_orders/",views.add_to_picked_up_orders),
    path("add_to_dropped_off_orders/",views.add_dropped_off_orders),
    path("order/<int:id>/update/",views.update_order),
    path("order/<int:id>/delete/",views.delete_order),
]