from django.urls import path
from . import views

urlpatterns =[
    path("item_to_cart/<int:id>/",views.item_to_cart),
    path("item_check_out/<str:pm>/<str:dm>/<str:drop_loc_lat>/<str:drop_off_lng>/<str:unique_code>/<str:total_price>/",views.item_check_out),
    # path("add_item_to_cart/<int:id>/",views.add_item_to_cart),
    path("remove_item_from_cart/<int:id>/",views.remove_item_from_cart),
    path("increase_item_quantity/<int:id>/",views.increase_item_quantity),
    path("decrease_item_quantity/<int:id>/",views.decrease_item_quantity),
    path("get_not_ordered_items/",views.get_not_ordered_items),
    path("get_ordered_items/",views.get_ordered_items),
    # path("check_out_order_items/",views.check_out_order_items),
    path("clear_order_items/",views.clear_order_items),

#     new order items
    path("get_my_ordered_items/",views.get_my_ordered_items)
]