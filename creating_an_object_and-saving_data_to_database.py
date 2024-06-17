from django.db import models

class Entry(models.Model):
      name = models.CharField(max_length=100)
      genre = models.CharField(max_length = 50)
      publication_year = models.IntegerField()


entry = Entry.objects.create(name="Good Name", genre = "rock", publication_year="2018")
