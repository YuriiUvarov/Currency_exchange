from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from currency_exchange import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
