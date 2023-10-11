from django.urls import path

from . import views

urlpatterns =[
    path("add_to_cart/<int:id>/",views.add_item_to_cart),
    path("get_all_my_cart_items/",views.get_all_my_cart_items),
    path("clear_cart/",views.clear_cart),
    path("cart/<int:id>/delete/",views.delete_item_from_cart),
    path("cart/<int:id>/increase/",views.increase_item_quantity),
    path("cart/<int:id>/decrease/",views.decrease_item_quantity),
]