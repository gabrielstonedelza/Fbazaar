from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path("users/",views.get_users),
    path("customers/",views.get_all_customers),
    path("drivers/",views.get_all_drivers),
    path("stock_managers/",views.get_all_stock_managers),
    path("send_otp/<str:otp>/<str:email>/<str:username>/",views.send_otp),
    path("get_admin/",views.get_admin),
    path("managers/",views.get_all_wholesale_managers),
    path("user/<int:id>/update/",views.update_user),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]