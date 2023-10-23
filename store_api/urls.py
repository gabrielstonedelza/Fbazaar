from django.urls import path

from . import views

urlpatterns = [
    path("add_item/",views.add_item),
    path("items/",views.get_all_items),
    path("exclusive_items/",views.get_exclusive_items),
    path("promotion_items/",views.get_promotion_items),
    path("other_items/",views.get_other_items),
    path("get_drinks/",views.get_drinks),
    path("get_water/",views.get_water),
    path("items/<int:id>/detail/",views.get_item_detail),
    path("items/<int:id>/update/",views.update_item),
    path("items/<int:id>/delete/",views.delete_item),

    path("add_to_price_change/",views.add_to_price_change),

    path("add_remarks/<int:id>/",views.add_remarks),
    path("remarks/",views.get_all_remarks),
    path("remark/<int:id>/delete",views.delete_remark),

    path("add_rating/",views.add_rating),
    path("ratings/",views.get_all_ratings),

    path("item/<int:id>/ratings/",views.get_all_item_ratings),
    path("item/<int:id>/remarks/",views.get_all_item_remarks),

    path("search_item/",views.SearchForItem.as_view()),
]