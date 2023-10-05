from django.urls import path

from . import views

urlpatterns = [
    path("profile/",views.profile),
    path("profile/<int:id>/update/",views.update_profile),
]