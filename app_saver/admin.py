from django.contrib import admin
from .models import *


class SavedImageAdmin(admin.ModelAdmin):
    list_display = ("__str__", "saved_at")
    search_fields = ("name",)


class UnsplashDailyLoadAdmin(admin.ModelAdmin):
    list_display = ("__str__", "loaded_images")
    search_fields = ("day",)


admin.site.register(SavedImage, SavedImageAdmin)
admin.site.register(UnsplashDailyLoad, UnsplashDailyLoadAdmin)
