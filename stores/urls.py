from django.urls import path

from . import views

urlpatterns = [
    path("register_store/",views.register_store),
    path("get_my_store/",views.get_my_store),
    path("get_all_stores/",views.get_all_stores),
    path("update_store/<int:id>/",views.update_store),
]