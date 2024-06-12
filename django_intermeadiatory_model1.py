from django.db import models

class Mango(models.Model):
    color = models.CharField(max_length=128)
    mango_from = models.CharField(max_length=128)  # Corrected typo here

class Person(models.Model):
    name = models.CharField(max_length=80)
    # Removed the mango_color ForeignKey, as it's redundant with the M2M relationship
    bought = models.ManyToManyField('Mango', through='Purchase')

class Purchase(models.Model):
    mango = models.ForeignKey('Mango', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    date = models.DateField()
    # Consider if you need the 'friends' field here or if it should be part of a different model/relationship
