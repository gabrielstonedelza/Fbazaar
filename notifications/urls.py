from django.urls import path

from . import views

urlpatterns = [
    path("my_notifications/",views.get_my_notifications),
    path("triggered_notifications/",views.get_my_triggered_notifications),
    path("read_notification/<int:id>/",views.read_notification),
    path("notification_detail/<int:id>/",views.get_notification_detail),
]