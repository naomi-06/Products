from django.contrib import admin
from django.urls import path, include
from app import views
urlpatterns = [
    path('', include('shop_backend.urls')),
    path('admin/', admin.site.urls),
    path('shop/', include('shop_backend.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
