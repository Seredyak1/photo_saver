import os
from datetime import date
from django.db import models
from django.conf import settings
from jsonfield import JSONField


def get_image_path(instance, filename):
    if settings.USE_S3_STORAGE:
        return os.path.join(settings.MEDIAFILES_LOCATION, f"{date.today()}/", filename)
    else:
        return os.path.join(f"{instance.saved_at}/", filename)


class ImagesTopic(models.Model):

    name = models.TextField()
    slug_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    external_id = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def images_count(self):
        count = SavedImage.objects.filter(topic=self).count()
        return count


class SavedImage(models.Model):

    name = models.TextField()
    topic = models.ForeignKey(ImagesTopic, on_delete=models.SET_NULL, blank=True, null=True)

    external_id = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=32, blank=True, null=True)
    downloads_count = models.IntegerField(blank=True, null=True)
    user = JSONField(blank=True, null=True)

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
