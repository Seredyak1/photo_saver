from datetime import datetime, timedelta
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import SavedImage, UnsplashDailyLoad
from .serializers import SavedImageSerializer
from .filters import SavedImageFilter
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


@api_view(("POST",))
def load_new_images(request, *args, **kwargs):
    last_daily_load = UnsplashDailyLoad.objects.all().order_by("created_at").last()
    if last_daily_load and last_daily_load.last_load_time:
        time_diff = int(datetime.now().timestamp() - last_daily_load.last_load_time.timestamp())
        if time_diff < 3660:
            time_less = 3660 - time_diff
            return Response({"error": "Less one hour from last load!", "seconds": time_less},
                            status=status.HTTP_400_BAD_REQUEST)

    load_images.delay()
    return Response({"detail": "Loading start"}, status=status.HTTP_201_CREATED)
