import os
from django.db import models
from django.conf import settings


def get_image_path(instance, filename):
    return os.path.join(f"{instance.saved_at}/", filename)


class SavedImage(models.Model):

    name = models.TextField()
    external_id = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    full_image = models.ImageField(upload_to=get_image_path)
    small_image = models.ImageField(upload_to=get_image_path)
    size = models.IntegerField(blank=True, null=True)
    saved_at = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class UnsplashDailyLoad(models.Model):

    day = models.DateField()
    loaded_images = models.IntegerField(default=0)
    last_load_time = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Load at {self.day}"
