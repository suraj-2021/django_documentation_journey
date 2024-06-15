from django.db import models

class vo2max(models.Model):
    oxygen_consumption = models.CharField(max_length=20)
    lungs_volume = models.CharField(max_length=10)
    HIT_length = models.DurationField()

class FitnessLength(vo2max):
    class Meta:
        proxy = True
