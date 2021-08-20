from rest_framework import serializers
from .models import *


class SavedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedImage
        fields = "__all__"
