from django.urls import path

from . import views

urlpatterns = [
    path("get_ordered_items/<str:unique_code>/",views.get_ordered_items),
    path("get_ordered_items_admin/<str:unique_code>/",views.get_ordered_items_admin)
]