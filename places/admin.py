from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ['get_preview']

    def get_preview(self, obj):
        max_height = 200
        return format_html(
            '<img src="{}" style="max-height:{}px" />',
            obj.imgs.url,
            max_height
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
