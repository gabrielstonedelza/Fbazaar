from django.urls import path

from . import views

urlpatterns = [
    path("my_orders/",views.get_my_orders),
    path("check_out/<int:id>/",views.check_out_items),
    path("get_cart_items/",views.get_cart_items),
    path("get_ordered_items/",views.get_ordered_items),
    path("check_out_items/",views.check_out_items),
    path("get_my_delivered_order/",views.get_my_delivered_order),
    path("pending_orders/",views.get_all_pending_orders),
    path("processing_orders/",views.get_all_processing_orders),
    path("picked_up_orders/",views.get_all_piked_up_orders),
    path("get_all_in_transit_orders/",views.get_all_in_transit_orders),
    path("get_customers_order_in_transit/",views.get_customers_order_in_transit),
    path("delivered_orders/",views.get_all_delivered_orders),
    path("clear_order/",views.add_to_cleared),
    path("cleared_orders/",views.get_cleared_for_pickup),
    path("picked_up_orders/",views.get_orders_picked_up),
    path("dropped_off_orders/",views.get_orders_dropped_off),
    path("add_to_picked_up_orders/",views.add_to_picked_up_orders),
    path("add_order_to_in_transit/",views.add_order_to_in_transit),
    path("add_to_dropped_off_orders/",views.add_dropped_off_orders),
    path("order/<int:id>/update/",views.update_order),
    path("order/<int:id>/delete/",views.delete_order),

#
    path("get_all_my_pending_orders/",views.get_all_my_pending_orders),
    path("get_all_my_processing_orders/",views.get_all_my_processing_orders),
    path("get_all_my_picked_up_orders/",views.get_all_my_picked_up_orders),
    path("get_all_my_delivered_orders/",views.get_all_my_delivered_orders),
#

    path("assign_driver_to_order/<int:id>/",views.assign_driver_to_order),
    path("get_all_my_assigned_orders/",views.get_all_my_assigned_orders),
    path("get_all_drivers_assigned_orders/",views.get_all_drivers_assigned_orders),

#
    path("add_drivers_current_location/<int:id>/",views.add_drivers_current_location),
    path("get_drivers_current_location/<int:id>/",views.get_drivers_current_location),
]