from django.urls import path

from . import views

urlpatterns = [
    path("add_to_favorites/<int:id>/",views.add_item_to_favorites),
    path("favorites/",views.get_all_my_fav_items),
    path("favorite/<int:id>/remove/",views.delete_item_from_favorites),
]