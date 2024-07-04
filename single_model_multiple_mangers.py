from django.db import models

class RussianManager(models.Manager):
    def get_queryset(self):
        return self.filter(northern_hemisphere="Russia")

class MongolianManager(models.Manager):
    def get_queryset(self):
        return self.filter(northern_hemisphere="Mongolia")

class AustralianManager(models.Manager):
    def get_queryset(self):
        return self.filter(southern_hemisphere="Australia")

class Earth(models.Model):
    NORTHERN_COUNTRIES = {
        "R": "Russia",
        "M": "Mongolia",
        "U": "Ukraine",
        "I": "Iceland",
        "Ir": "Ireland",
        "P": "Poland",
        "C": "Canada",
    }

    SOUTHERN_COUNTRIES = {
        "J": "Japan",
        "A": "Australia",
        "In": "India",
        "C": "Chile",
        "Ar": "Argentina",
        "B": "Brazil",
        "P": "Panama",
        "S": "South Africa",
        "M": "Mexico",
    }

    northern_hemisphere = models.CharField(max_length=2, choices=NORTHERN_COUNTRIES.items())
    southern_hemisphere = models.CharField(max_length=2, choices=SOUTHERN_COUNTRIES.items())
    description = models.TextField()

    objects = models.Manager()
    australia = AustralianManager()
    mongolian = MongolianManager()
    russia = RussianManager()

peoples = Earth.australia.all()

for people in peoples:
    print(f"Country: {people.northern_hemisphere}, Description: {people.description}")
