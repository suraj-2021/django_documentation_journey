from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Planets(models.Model):
    name = models.CharField(max_length=30, verbose_name="Planet Name", help_text="Name of the planet")
    diameter = models.IntegerField(verbose_name="Diameter in kilometers")
    moons = models.IntegerField(validators=[MinValueValidator(0)], verbose_name="Number of Moons")

    class Meta:
        abstract = True

class Project(Planets):
    project_name = models.CharField(max_length=150, verbose_name="Project Name")
    project_budget = models.IntegerField(verbose_name="Project Budget in USD")

    def __str__(self):
        return self.project_name
