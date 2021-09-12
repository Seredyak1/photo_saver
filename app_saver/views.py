from datetime import datetime
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import SavedImage, ImagesTopic, UnsplashDailyLoad
from .serializers import SavedImageSerializer, ImagesTopicSerializers
from .filters import SavedImageFilter, ImageTopicFilter
from .tasks import load_images


class SavedImageAPIView(generics.ListAPIView):
    """
    get:
    Return all campaigns list
    post:
    Create new campaign
    """
    serializer_class = SavedImageSerializer
    queryset = SavedImage.objects.all().order_by("-saved_at")
    filter_backends = (DjangoFilterBackend,)
    filter_class = SavedImageFilter


class ImageTopicListAPIView(generics.ListAPIView):
    serializer_class = ImagesTopicSerializers
    queryset = ImagesTopic.objects.all().order_by("-created_at")
    filter_backends = (DjangoFilterBackend,)
    filter_class = ImageTopicFilter


@swagger_auto_schema(
    method='post',
    manual_parameters=[
        openapi.Parameter('topic_name', openapi.IN_QUERY,
                          description="Topic name for load images with this topic relations",
                          type=openapi.TYPE_STRING,
                          required=False)
    ]
)
@api_view(("POST",))
def load_new_images(request, *args, **kwargs):
    last_daily_load = UnsplashDailyLoad.objects.all().order_by("created_at").last()
    if last_daily_load and last_daily_load.last_load_time:
        time_diff = int(datetime.now().timestamp() - last_daily_load.last_load_time.timestamp())
        if time_diff < 3660:
            time_less = 3660 - time_diff
            return Response({"error": "Less one hour from last load!", "seconds": time_less},
                            status=status.HTTP_400_BAD_REQUEST)

    topic = request.GET.get("topic_name", None)
    load_images.delay(topic)
    return Response({"detail": "Loading start"}, status=status.HTTP_201_CREATED)
