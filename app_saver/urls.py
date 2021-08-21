from django.urls import path, include
from .views import SavedImageAPIView, load_new_images

urlpatterns = [
    path("images/", SavedImageAPIView.as_view()),
    path("load_new_images/", load_new_images),
]
