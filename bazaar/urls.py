
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from users.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('notifications/', include('notifications.urls')),
    path('profile/', include('profiles.urls')),
    path('store_api/', include('store_api.urls')),
    path('store/', include("stores.urls")),
    path('users/', include("users.urls")),
    path('order/', include("orders.urls")),
    path('cart/', include("cart.urls")),
    path('favorites/', include("favorites.urls")),
    path("",home,name="home"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
