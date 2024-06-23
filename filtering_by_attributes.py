from django.db import models

class University(models.Model):
    name = models.CharField(max_length=150)
    headline = models.TextField()  # Adjusted field type if needed
    establishment_date = models.DateField()

universe = University.objects.filter(establishment_date__year=2014)


universe_gte_2014 = University.objects.filter(establishment_date__year__gte=2014)
