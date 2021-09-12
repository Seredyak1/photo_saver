from django.db.models import Q

from django_filters import rest_framework as filters
from .models import SavedImage, ImagesTopic


class SavedImageFilter(filters.FilterSet):
    """Filters for TimeWeek object"""
    date = filters.DateFilter(field_name="saved_at")
    search = filters.CharFilter(method="search_filter")
    topic = filters.NumberFilter(field_name="topic_id")

    class Meta:
        model = SavedImage
        fields = ('date', "search", 'topic')

    def search_filter(self, queryset, *args, **kwargs):
        search_query = self.request.query_params.get('search')
        queryset = queryset.filter(Q(name__icontains=search_query) |
                                   Q(description__icontains=search_query))
        return queryset


class ImageTopicFilter(filters.FilterSet):
    search = filters.CharFilter(method="search_filter")

    class Meta:
        model = ImagesTopic
        fields = ("search",)

    def search_filter(self, queryset, *args, **kwargs):
        search_query = self.request.query_params.get('search')
        queryset = queryset.filter(Q(name__icontains=search_query) |
                                   Q(description__icontains=search_query))
        return queryset
