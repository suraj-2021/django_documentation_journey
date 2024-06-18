from django.db.models import F
from django.db import models


class BigMountains(models.Model):
      name = models.CharField(max_legth=150)
      height = models.IntegerField()
      peak_temprature = models.IntegerField()
      climbers = models.IntegerField()


mountains = BigMountains.objects.filter(peak_temprature__lt=F("climbers"))
