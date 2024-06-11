from django.db import models


class Person(models.Model):
  shirt_sizes = {
      "S": "small",
      "M": "medium",
      "L": "Large",
      "XL": "ExtraLarge",
  }
  name = models.CharField(max_length=50)
  shirt_size = models.CharField(max_length=2, choices=shirt_sizes)
