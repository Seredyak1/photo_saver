from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ['*']
DEBUG = os.environ.get("DEBUG", False)
SECRET_KEY = os.environ.get("SECRET_KEY", False)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', 'db_image_saver'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASS', 'postgres'),
        'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
        'PORT': '5432',
    }
}

USE_HASHED_TOKEN = os.environ.get('TOKEN_KEY', True)
TOKEN_KEY = os.environ.get('TOKEN_KEY', "As1x64")

USE_S3_STORAGE = os.environ.get("USE_S3_STORAGE", False)

if USE_S3_STORAGE:

    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', '')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_S3_ACCESS_KEY_ID', '')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_S3_SECRET_ACCESS_KEY', '')
    AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME', '')
    AWS_S3_ADDRESSING_STYLE = "path"
    AWS_S3_CUSTOM_DOMAIN = "{}.s3.amazonaws.com".format(AWS_STORAGE_BUCKET_NAME)
    AWS_S3_FILE_OVERWRITE = False
    AWS_PATH = os.environ.get('AWS_PATH', 'development')
    AWS_S3_ENV_MEDIA_NAME = os.environ.get('AWS_S3_ENV_MEDIA_NAME', 'development/')

    STATICFILES_LOCATION = 'static'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATIC_URL = 'https://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

    MEDIAFILES_LOCATION = 'media'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    MEDIA_URL = 'https://{}/{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, AWS_S3_ENV_MEDIA_NAME, MEDIAFILES_LOCATION)

else:
    STATIC_URL = '/static/'
    STATIC_ROOT = 'static/'
    MEDIA_URL = '/media/'
    MEDIA_ROOT = 'media/'

UNSPLASH_ACCESS_KEY = os.environ.get('UNSPLASH_ACCESS_KEY', "")
UNSPLASH_SECRET_KEY = os.environ.get('UNSPLASH_SECRET_KEY', "")
