from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("users/",views.get_users),
    path("user/<int:id>/update/",views.update_user),
]