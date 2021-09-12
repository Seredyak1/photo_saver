from rest_framework import serializers
from .models import *


class SavedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedImage
        fields = "__all__"


class ImagesTopicSerializers(serializers.ModelSerializer):
    images_count = serializers.SerializerMethodField()

    class Meta:
        model = ImagesTopic
        fields = "__all__"

    def get_images_count(self, instance, *args, **kwargs):
        return instance.images_count
