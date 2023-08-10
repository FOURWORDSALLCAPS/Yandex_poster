from django.contrib import admin
from django.urls import path
from places.views import show_place, show_index
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_index),
    path('place/<int:place_id>', show_place, name='show_place'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
