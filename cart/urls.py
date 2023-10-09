from django.urls import path

from . import views

urlpatterns =[
    path("add_to_cart/",views.add_item_to_cart),
    path("get_all_my_cart_items/",views.get_all_my_cart_items),
    path("cart/<int:id>/update/",views.update_my_cart),
    path("cart/<int:id>/delete/",views.delete_item_from_cart),
]