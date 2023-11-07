from django.urls import path

from . import views

urlpatterns = [
    path("get_ordered_items/",views.get_ordered_items)
]