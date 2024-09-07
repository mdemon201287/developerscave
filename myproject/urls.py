# myproject/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),  # Frontend URLs
    path('api/', include('shop.api_urls')),  # API URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Add this line

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
