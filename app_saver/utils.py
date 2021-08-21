import io
import requests
from datetime import date
from django.conf import settings
from django.core.files.images import ImageFile

from .models import UnsplashDailyLoad, SavedImage


class UnsplashPhotoLoader:
    def __init__(self):
        self.date_today = date.today()
        self.client_id: str = settings.UNSPLASH_ACCESS_KEY
        self.client_secret: str = settings.UNSPLASH_SECRET_KEY
        self.daily_load: UnsplashDailyLoad = self.__get_daily_load_log()

        self.page = 1
        self.api_url = 'https://api.unsplash.com/'
        self.current_load = 0

    @property
    def headers(self):
        headers = {"Authorization": f"Client-ID {self.client_id}"}
        return headers

    def __get_daily_load_log(self):
        dl, s = UnsplashDailyLoad.objects.get_or_create(day=self.date_today)
        return dl

    def __save_image(self, image_url: str, image_description: str):
        img_res = requests.get(image_url, stream=True)
        img_content = img_res.content
        name = image_url.split("/")[-1].split("?")[0]
        image = ImageFile(io.BytesIO(img_content), name=f'{name}.jpg')

        SavedImage.objects.create(name=name, saved_at=self.date_today,
                                  description=image_description, image=image)

    def __get_images_list(self) -> dict:
        """
        max el in page = 30
        """
        endpoint = f'photos?page={self.page}&per_page=30'
        res = requests.get(self.api_url + endpoint, headers=self.headers)
        if res.status_code != 200:
            raise Exception("Response error: ", res.text)

        images_res = res.json()
        return images_res

    def load_new_images(self):
        # todo add right values
        while self.page < 2:
            images_res = self.__get_images_list()

            for image in images_res:
                image_urls = image.get("urls", None)
                if not image_urls:
                    pass
                else:
                    image_description = image['description']
                    image_url = image_urls.get("full")
                    self.__save_image(image_url, image_description)
                    self.current_load += 1

            self.daily_load.loaded_images = self.current_load
            self.daily_load.save()
