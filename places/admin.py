from django.contrib import admin
from .models import Place, Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
