from django.urls import path
from . import views

urlpatterns =[
    path("add_item_to_cart/<int:id>/",views.add_item_to_cart),
    path("get_not_ordered_items/",views.get_not_ordered_items),
    path("get_ordered_items/",views.get_ordered_items),
    path("check_out_order_items/",views.check_out_order_items),
]