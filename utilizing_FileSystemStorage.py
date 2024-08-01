from django.core.files.storage import FileSystemStorage
from django.db import models

fs = FileSystemStorage(location = "/media/photos")
class my_db(models):
      photo = models.ImageField(storage = fs)
