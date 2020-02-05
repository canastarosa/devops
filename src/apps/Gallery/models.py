from django.conf import settings
from django.db import models

from utils.files import path_and_rename


class Image(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    file = models.ImageField(upload_to=path_and_rename('featured/market/banner/'))
