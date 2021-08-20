from datetime import date

from django_filters import rest_framework as filters
from .models import SavedImage


class SavedImageFilter(filters.FilterSet):
    """Filters for TimeWeek object"""
    date = filters.DateFilter(field_name="saved_at")
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = SavedImage
        fields = ('date', "name",)
