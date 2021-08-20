from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status

from .models import SavedImage
from .serializers import SavedImageSerializer
from .filters import SavedImageFilter


class SavedImageAPIView(generics.ListAPIView):
    """
    get:
    Return all campaigns list
    post:
    Create new campaign
    """
    serializer_class = SavedImageSerializer
    queryset = SavedImage.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = SavedImageFilter
