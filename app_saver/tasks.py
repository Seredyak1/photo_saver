from photo_saver.celery import app

from app_saver.utils import UnsplashPhotoLoader


@app.task
def load_images(topic_name: str or None =None):
    """Start loading new images into DB"""
    if topic_name:
        UnsplashPhotoLoader().load_new_image_with_topic(topic_name)
    else:
        UnsplashPhotoLoader().load_new_images()
