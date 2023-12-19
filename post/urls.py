# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('all-posts/', views.get_all_post),
    path('create-post/', views.add_post),
    # Add other URLs as needed
]
