from django.db import models

class InfoClass(models.Model):
    name = models.CharField(max_length=50)
    identification_code = models.CharField(max_length=20)

    class Meta:
        abstract = True
        ordering = ['name']

class SimpleClass(models.Model):
    class Meta:
        abstract = True
        managed = False

class Person(InfoClass, SimpleClass):
    status = models.CharField(max_length=200)

    class Meta:
        ordering = InfoClass.Meta.ordering
        managed = SimpleClass.Meta.managed
