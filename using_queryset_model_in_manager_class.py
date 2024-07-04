from django.db import models

class EarthQuerySet(models.QuerySet):
    def country(self):
        return self.filter(country_population__gt=200000000)

    def continent(self):
        return self.filter(continent_population__gt=500000000)

class EarthManager(models.Manager):
    def get_queryset(self):
        return EarthQuerySet(self.model, using=self._db)

class Earth(models.Model):
    country_name = models.CharField(max_length=150)
    country_population = models.IntegerField()
    continent_name = models.CharField(max_length=150)
    continent_population = models.IntegerField()

    details = EarthManager()
