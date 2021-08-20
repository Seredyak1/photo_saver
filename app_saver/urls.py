from django.urls import path, include
from .views import SavedImageAPIView

urlpatterns = [
    path("images/", SavedImageAPIView.as_view()),
]
