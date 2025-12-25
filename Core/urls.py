from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    # Media dosyalarını (resim vb.) sunmak için
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    # Static dosyaları sunmak için (Bazen gerekmez ama garanti olsun)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
