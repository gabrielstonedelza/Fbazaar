from django.urls import path

from . import views

urlpatterns = [
    path("add_item/",views.add_item),
    path("items/",views.get_all_items),
    path("items/<int:id>/update/",views.update_item),
    path("items/<int:id>/delete/",views.delete_item),

    path("add_to_price_change/",views.add_to_price_change),

    path("add_remarks/",views.add_remarks),
    path("remarks/",views.get_all_remarks),
    path("remark/<int:id>/delete",views.delete_remark),

    path("add_rating/",views.add_rating),
    path("ratings/",views.get_all_ratings),
]