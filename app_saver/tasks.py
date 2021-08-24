from photo_saver.celery import app

from app_saver.utils import UnsplashPhotoLoader


@app.task
def load_images():
    """Start loading new images into DB"""
    UnsplashPhotoLoader().load_new_images()
