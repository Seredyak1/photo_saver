from django.contrib import admin
from .models import *


class SavedImageAdmin(admin.ModelAdmin):
    list_display = ("__str__", "topic", "saved_at")
    search_fields = ("name", "topic__name")


class ImagesTopicAdmin(admin.ModelAdmin):
    list_display = ("__str__", "created_at")
    search_fields = ("name",)


class UnsplashDailyLoadAdmin(admin.ModelAdmin):
    list_display = ("__str__", "loaded_images")
    search_fields = ("day",)


admin.site.register(SavedImage, SavedImageAdmin)
admin.site.register(ImagesTopic, ImagesTopicAdmin)
admin.site.register(UnsplashDailyLoad, UnsplashDailyLoadAdmin)
