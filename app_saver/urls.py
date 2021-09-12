from django.urls import path
from .views import SavedImageAPIView, ImageTopicListAPIView, load_new_images

urlpatterns = [
    path("images/", SavedImageAPIView.as_view()),
    path("topics/", ImageTopicListAPIView.as_view()),

    path("load_new_images/", load_new_images),
]
