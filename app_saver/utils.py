import io
import requests
from datetime import datetime, date
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

    def __save_image(self, image_element: dict):
        external_id = image_element.get("id")
        image_description = image_element['description']
        full_url = image_element.get("urls", {}).get("full", "")
        name = full_url.split("/")[-1].split("?")[0]

        full_img_res = requests.get(full_url, stream=True)
        full_img_content = full_img_res.content
        full_image = ImageFile(io.BytesIO(full_img_content), name=f'{name}_full.jpg')

        small_url = image_element.get("urls", {}).get("small", "")
        small_img_res = requests.get(small_url, stream=True)
        small_img_content = small_img_res.content
        small_image = ImageFile(io.BytesIO(small_img_content), name=f'{name}_small.jpg')

        SavedImage.objects.create(external_id=external_id, name=name, saved_at=self.date_today,
                                  description=image_description,
                                  full_image=full_image, small_image=small_image)

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
        while self.page < 41:
            images_res = self.__get_images_list()

            for image in images_res:
                try:
                    self.__save_image(image)
                    self.current_load += 1
                except Exception as e:
                    print(e)

            self.daily_load.loaded_images = self.current_load
            self.daily_load.last_load_time = datetime.now()
            self.daily_load.save()

            self.page += 1
