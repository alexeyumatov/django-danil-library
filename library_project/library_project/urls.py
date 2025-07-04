from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from . import settings
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('auth/', include('authorization.urls')),
    path('books/', include('books.urls')),
    path('orders/', include('orders.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
