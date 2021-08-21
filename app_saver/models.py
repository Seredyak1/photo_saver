import os
from django.db import models
from django.conf import settings


def get_image_path(instance, filename):
    return os.path.join(f"{instance.saved_at}/", filename)


class SavedImage(models.Model):

    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=get_image_path)
    size = models.IntegerField(blank=True, null=True)
    saved_at = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class UnsplashDailyLoad(models.Model):

    day = models.DateField()
    loaded_images = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Load at {self.day}"
